from flask import Flask, request, redirect, url_for, Response, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import secrets
import jwt
import secrets
import datetime

app = Flask(__name__)
CORS(app, expose_headers='Authorization', resources={r"/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/Tobias/Desktop/Bachelorarbeit/Code/SurveyPage/SurveyBackendEnv/database/meta.db'
db = SQLAlchemy(app)
meta_keys = ["firstName","lastName","dateOfBirth","nativeLanguage","dateTime","sessionID"]

secret_key = secrets.token_hex(16)
# app.config['SECRET_KEY'] = secret_key
app.config['SECRET_KEY'] = 'secret'


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
          'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=1),
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


def saveSoundfile(data):
    #todo
    return True


def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return payload
    except jwt.ExpiredSignatureError:
        return {'msg':'Signature expired. Please log in again.'}, 403
    except jwt.InvalidTokenError:
        return {'msg':'Invalid token. Please log in again.'}, 403


def get_token(bearer_token):
    PREFIX = 'Bearer '
    if not bearer_token.startswith(PREFIX):
        return None
    return bearer_token[len(PREFIX):]


@app.route('/meta', methods=['PUT'])
def meta():
    meta_data = request.json
    if request.method == 'PUT' and validate_json_payload(meta_data, meta_keys):


        # to-do: put that shit in a database with saveMeta

        token = encode_auth_token(meta_data).decode()

        return {"token": token}, 200
    else:
        return {"msg": "Missing keys or wrong request method"}, 403



@app.route('/soundfile', methods=['PUT'])
def soundfile():
    bearer_token = request.headers['Authorization']
    token_string = get_token(bearer_token)


    if request.method == 'PUT' and token_string:

        token_bytes = token_string.encode()
        token_json = decode_auth_token(token_bytes)

        print(token_json)

        print(token_json['firstName'])
        print(token_json['lastName'])


        # to-do: write payload into if-not-exists new folder with saveSoundfile

        return {'msg': "Successfully submitted Soundfile"}, 200
    else:
        return {'msg':'Wrong request method or failed authorization'}, 403







if __name__ == '__main__':


    app.run(host='127.0.0.1', port=1337, debug=True)