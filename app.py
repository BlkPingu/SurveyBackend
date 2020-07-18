from flask import Flask, request, redirect, url_for
import jwt
from flask_cors import CORS
from api import decode_auth_token
from flask_sqlalchemy import SQLAlchemy





app = Flask(__name__)
CORS(app, expose_headers='Authorization', resources={r"/api/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/Tobias/Desktop/Bachelorarbeit/Code/SurveyPage/SurveyBackendEnv/database/meta.db'
db = SQLAlchemy(app)



# This will let us Create a new book and save it in our database
@app.route('/meta', methods=['PUT'])
def meta():
    if request.method == 'PUT':
        auth_token = request.headers.get('Authorization')
        payload = decode_auth_token(auth_token, app)
        print(payload)

        # nimm token und decode
        # wenn decode ok
        # check payload
        # wenn ok write und 200
        # wenn schrott 403

        return Response(status=200)
    else: return Response(status=403)

@app.route('/soundfile', methods=['PUT'])
def soundfile():
    if request.method == 'PUT':
        auth_token = request.headers.get('authorization')
        payload = decode_auth_token(auth_token, app)
        print(payload)

        # nimm token und decode
        # wenn decode ok
        # check payload
        # wenn ok write und 200
        # wenn schrott 403

        return Response(status=200)
    else: return Response(status=403)


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