import secrets

class Config(object):
    DEBUG = True
    SECRET_KEY = "secret"
    HOST = '127.0.0.1'
    PORT = 1337
    SOUNDFILE_UPLOAD = "/home/username/projects/my_app/app/static/images/uploads"
    SQLALCHEMY_DATABASE_URI = 'sqlite://///Users/Tobias/Desktop/Bachelorarbeit/Code/SurveyPage/SurveyBackendEnv/database/meta.db'


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = secrets.token_hex(16)
    SOUNDFILE_UPLOAD = "/home/username/app/app/static/images/uploads"
    HOST = '46.101.246.133'
    PORT = 5000
    DATABASE = 'path'

class DevelopmentConfig(Config):
    pass