from flask import Flask, request, redirect, url_for, Response, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import jwt
import datetime

app = Flask(__name__)


if app.config['ENV'] == 'production':
    app.config['DEBUG'] = False
    app.config['SECRET_KEY'] = 'brrr'
    app.config['SOUNDFILE_UPLOAD'] = '/srv/data/soundfiles'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///srv/data/database/meta.db'
else:
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'secret'
    app.config['SOUNDFILE_UPLOAD'] = 'sqlite://///Users/Tobias/Desktop/Bachelorarbeit/Code/SurveyPage/soundfiles'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/Tobias/Desktop/Bachelorarbeit/Code/SurveyPage/database/meta.db'




    print(f'ENV is set to: {app.config["ENV"]}')
    print(app.config['SECRET_KEY'])

CORS(app, expose_headers='Authorization', resources={r"/*": {"origins": "*"}})
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/Tobias/Desktop/Bachelorarbeit/Code/SurveyPage/SurveyBackendEnv/database/meta.db'
db = SQLAlchemy(app)
meta_keys = ["firstName","lastName","dateOfBirth","nativeLanguage","dateTime","sessionID"]

# app.config['SECRET_KEY'] = secret_key
# app.config['SECRET_KEY'] = 'secret'

# ssl_context=context
# from OpenSSL import SSL
# context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
# context.use_privatekey_file('server.key')
# context.use_certificate_file('server.crt')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Meta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), primary_key=True)
    time_created = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    token = db.Column(db.String(200), unique=True)

    def __repr__(self):
        return '<Session %r>' % self.session

def encode_auth_token(payload):
    signed_token = {
          'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=600),
          'iat': datetime.datetime.utcnow(),
          'firstName':payload['firstName'],
          'lastName':payload['lastName'],
          'dateOfBirth':payload['dateOfBirth'],
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


def validate_json_payload(meta_keys, meta_data):
  for key in meta_keys:
    if key not in meta_data:
      return False
  return True


def saveMeta(json):
    #to-do
    return True


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
    meta_data = request.json
    if request.method == 'PUT' and validate_json_payload(meta_data, meta_keys):


        # to-do: put that shit in a database with saveMeta
        token = encode_auth_token(meta_data).decode() # b'abc123' -> "abc123"
        print(token)
        return {'token':token}, 200
    else:
        return {'msg': 'Missing keys or wrong request method'}, 403



@app.route('/audio', methods=['POST'])
def soundfile():

    if request.method == 'POST':

        try:
            bearer_token = request.headers['Authorization']
        except KeyError:
            return {'msg':'No token.'}, 403

        if bearer_token:
            token_string = get_token(bearer_token)
        else: return {'msg':'No token.'}, 403

        token_bytes = token_string.encode()

        try:
            payload = jwt.decode(token_bytes, app.config['SECRET_KEY'])

        except jwt.ExpiredSignatureError:
            return {'msg':'Signature expired. Please log in again.'}, 403
        except jwt.InvalidTokenError:
            return {'msg':'Invalid token. Please log in again.'}, 403

        if request['filename']:
            pass

        if foldername['filename']:
            pass

        if 'audio' in request.files:
            filename = images.save(request.files['audio'])
            image_filename = filename
            image_url = images.url(filename)



        print(payload)
        print(token_json['firstName'])
        print(token_json['lastName'])

        # to-do: write payload into if-not-exists new folder with saveSoundfile

        return {'msg': "Successfully submitted Soundfile"}, 200
    else:
        return {'msg':'Wrong request method'}, 403



