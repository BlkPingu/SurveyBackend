from flask import Flask, request, redirect, url_for, Response
from flask_cors import CORS
from api import decode_auth_token
from flask_sqlalchemy import SQLAlchemy
import jwt
import secrets





app = Flask(__name__)
CORS(app, expose_headers='Authorization', resources={r"/api/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/Tobias/Desktop/Bachelorarbeit/Code/SurveyPage/SurveyBackendEnv/database/meta.db'
db = SQLAlchemy(app)
meta_keys = ["firstName","lastName","dateOfBirth","nativeLanguage","dateTime","sessionID"]

secret_key = secrets.token_hex(16)
# app.config['SECRET_KEY'] = secret_key
app.config['SECRET_KEY'] = 'secret'


def validate_json_payload(meta_keys, meta_data):
  for key in meta_keys:
    if key not in meta_data:
      return False
  return True


@app.route('/meta', methods=['PUT'])
def meta():
    meta_data = request.json
    if request.method == 'PUT' and validate_json_payload(meta_data, meta_keys):

        # to-do: put that shit in a database

        print(meta_data)

        token = encode_auth_token(meta_data)

        print(new_token)

        return {'token': str(token)}, 200
    else:
        return 403

@app.route('/soundfile', methods=['PUT'])
def soundfile():
    if request.method == 'PUT':
        token = request.authorization

        print(token)

        # payload = decode_auth_token(token)
        # print(payload)

        # nimm token und decode
        # wenn decode ok
        # check payload
        # wenn ok write und 200
        # wenn schrott 403

        return 200
    else:
      return 403


def encode_auth_token(payload):
    try:
        return jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'



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

def create_new_database(db):
    db.create_all()
    admin = User(username='admin', email='contact@tobiaskolb.dev')
    db.session.add(admin)
    db.session.commit()

def new_metadata(db, data):
    pass


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'm1uqfiDG.!KcgS%;E+QSrY%2+:m+6V'
    app.run(host='127.0.0.1', port=4996, debug=True)