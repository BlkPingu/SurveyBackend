from flask import Flask, request, redirect, url_for, Response, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import jwt
import datetime
from flask_cors import CORS,cross_origin
import os
import json


from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage



app = Flask(__name__)


if app.config['ENV'] == 'production':
    app.config['DEBUG'] = False
    app.config['SECRET_KEY'] = 'brrr'
    app.config['SOUNDFILE_UPLOAD'] = '/srv/data/soundfiles'
    app.config['METADATA_UPLOAD'] = '/srv/data/database'
else:
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'secret'
    app.config['SOUNDFILE_UPLOAD'] = '/Users/Tobias/Desktop/Bachelorarbeit/Code/SurveyPage/data/soundfiles'
    app.config['METADATA_UPLOAD'] = '/Users/Tobias/Desktop/Bachelorarbeit/Code/SurveyPage/data/database'


print(f'ENV is set to: {app.config["ENV"]}')
CORS(app, supports_credentials=True)

meta_keys = ['gender', 'age', 'nativeLanguage', 'dateTime', 'sessionID']

def encode_auth_token(payload):
    signed_token = {
          'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=3),
          'iat': datetime.datetime.utcnow(),
          'sessionID':payload['sessionID']
        }


    try:
        return jwt.encode(
            signed_token,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e


def validate_json_payload(meta_keys, metadata):
  for key in meta_keys:
    if key not in metadata:
      return False
  return True


def save_meta(metadata):
    directory = os.path.join(app.config['METADATA_UPLOAD'])
    session_id = metadata['sessionID']

    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    metadata = {
            'uuid': metadata['sessionID'],
            'age_range': metadata['age'],
            'request': metadata['nativeLanguage'],
            'gender': metadata['gender']
        }
    file_path = os.path.join(directory, secure_filename(session_id + '.json'))


    with open(file_path, 'w') as fp:
        json.dump(metadata, fp)

def get_token(bearer_token):
    PREFIX = 'Bearer '
    if not bearer_token.startswith(PREFIX):
        return None
    return bearer_token[len(PREFIX):]


@app.route('/xyz', methods=['GET'])
def generic():
    return {'msg':'hello i am flask'},  200



@app.route('/meta', methods=['PUT'])
def meta():
    metadata = request.json
    if request.method == 'PUT' and validate_json_payload(metadata, meta_keys):
        save_meta(metadata)

        token = encode_auth_token(metadata).decode()
        return {'token':token}, 200
    else:
        return {'msg': 'Missing keys or wrong request method'}, 403

def save_wav(directory, filename, file):
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    file_path = os.path.join(directory, secure_filename(filename + '.wav'))
    file.save(file_path)


def validate_token(request):
    try:
        bearer_token = request.headers['Authorization']

        token_string = get_token(bearer_token)
        token_bytes = token_string.encode()
        payload = jwt.decode(token_bytes, app.config['SECRET_KEY'])
        return payload
    except:
        print('token validation went wrong')
        return None




@app.route('/audio', methods=['POST'])
def soundfile():

    token_data = validate_token(request)
    file = request.files['audio']

    if request.method == 'POST' and token_data is not None and file is not None:

        filename = request.form['filename']
        foldername = request.form['foldername']
        directory = os.path.join(app.config.get('SOUNDFILE_UPLOAD'),foldername)

        save_wav(directory, filename, file)
        resp = Response('Soundfile submit worked')
        resp.headers['Access-Control-Allow-Origin'] = '*'

        return resp
    else:
        return {'msg':'Wrong request method or bad token'}, 403
