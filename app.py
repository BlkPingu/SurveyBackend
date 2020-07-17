from flask import Flask, request, redirect, url_for
import jwt
from api import decode_auth_token

app = Flask(__name__)


# This will let us Create a new book and save it in our database
@app.route('/meta', methods=['PUT'])
def meta():
    if request.method == 'PUT':
        auth_token = request.headers.get('authorization')
        payload = decode_auth_token(auth_token)
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
        payload = decode_auth_token(auth_token)
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