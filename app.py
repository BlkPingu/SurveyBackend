from flask import Flask, request, redirect, url_for
import jwt
from flask_cors import CORS
from api import decode_auth_token
from database import User, Meta, create_new_database, new_metadata
from flask_sqlalchemy import SQLAlchemy





app = Flask(__name__)
CORS(app, expose_headers='Authorization', resources={r"/api/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
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



if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'm1uqfiDG.!KcgS%;E+QSrY%2+:m+6V'
    app.run(host='127.0.0.1', port=4996, debug=True)