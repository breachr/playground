import os

class DevelopmentConfig(object):
    # Basic Setup
    ENV = 'development'                                     # set environment
    DEBUG = True                                            # enable debug mode
    # SEND_FILE_MAX_AGE_DEFAULT = 1                           # disable caching

    # Cookies
    SESSION_COOKIE_NAME = 'session'                         # changes the session cookies name (def: session)
    SESSION_COOKIE_DOMAIN = None                            # domain match rule
    SESSION_COOKIE_PATH = None
    SESSION_COOKIE_SECURE = False                           # only send cookies on secure connections

    # Keys
    SECRET_KEY = 'devo'                                      # secret key
    # SECRET_KEY = os.environ.get("KFZ_KEY")                  # secret key from environment

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(object):
    # Basic Setup
    ENV = 'production'                                      # set environment
    DEBUG = False                                           # enable debug mode
    # SEND_FILE_MAX_AGE_DEFAULT = 1                           # disable caching

    # Cookies
    SESSION_COOKIE_NAME = 'session'                         # changes the session cookies name (def: session)
    SESSION_COOKIE_DOMAIN = None                            # domain match rule
    SESSION_COOKIE_PATH = None
    SESSION_COOKIE_SECURE = False                           # only send cookies on secure connections

    # Keys
    SECRET_KEY = 'devo'                                      # secret key
    # SECRET_KEY = os.environ.get("KFZ_KEY")                  # secret key from environment

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
