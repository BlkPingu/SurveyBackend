

def saveMeta(json):
    #to-do
    return True


def saveSoundfile(data):
    #todo
    return True

@staticmethod
def decode_auth_token(auth_token, app):
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
