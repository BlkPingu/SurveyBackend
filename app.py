from flask import Flask, request, redirect, url_for
import jwt
from flask_cors import CORS

from api import decode_auth_token

app.config['SECRET_KEY'] = '\xbd\xd4\xc6L\x16)-xm<5\xf4Pi\xd5\xad.\x00\x1ek\xf3\xb4`\x8c@\xdc\xdfe\xd5 <\x05\xa0\xb9%\x16\xb3.z\xbb'
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


app = Flask(__name__)
CORS(app)

# This will let us Create a new book and save it in our database
@app.route('/meta', methods=['PUT'])
def meta():
    if request.method == 'PUT':
        auth_token = request.headers.get('authorization')
        payload = decode_auth_token(auth_token, app)
        print(payload)

        # nimm token und decode
        # wenn decode ok
        # check payload
        # wenn ok write und 200
        # wenn schrott 404

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
        # wenn schrott 404
        return Response(status=200)
    else: return Response(status=403)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4996, debug=True)