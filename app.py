from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# This will let us Create a new book and save it in our database
@app.route('/api/meta', methods=['PUT'])
def meta():
    if request.method == 'PUT':


        return Response(status=200)

@app.route('/api/soundfile', methods=['PUT'])
def soundfile():
    if request.method == 'PUT':


        return Response(status=200)



"""
api functions
"""

def saveMeta(json):
    #to-do
    return True


def saveSoundfile(data):
    #todo
    return True


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=4996)
