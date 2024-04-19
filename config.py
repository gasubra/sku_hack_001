# config.py

envfile = """FLASK_APP=sku_hack_001"""

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your-secret-key'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True