import secrets

class Config(object):
    FLASK_APP = 'app.py'
    DEBUG = True
    SECRET_KEY = 'secret'
    SOUNDFILE_UPLOAD = 'sqlite://///Users/Tobias/Desktop/Bachelorarbeit/Code/SurveyPage/soundfiles'
    SQLALCHEMY_DATABASE_URI = 'sqlite://///Users/Tobias/Desktop/Bachelorarbeit/Code/SurveyPage/database/meta.db'
    HOST = '127.0.0.1'
    PORT = 1337


class ProductionConfig(Config):
    FLASK_APP = 'app.py'
    DEBUG = False
    SECRET_KEY = '47f1da08191ed664aea40928f97c74ab' #secrets.token_hex(16)
    SOUNDFILE_UPLOAD = '/srv/data/soundfiles'
    SQLALCHEMY_DATABASE_URI = 'sqlite://///srv/data/database/meta.db'
    HOST = '46.101.246.133'
    PORT = 443

class DevelopmentConfig(Config):
    pass