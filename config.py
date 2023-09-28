# Configuration files for the API

class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///database.db'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'sqlite:///database.db' # MYSQL/PSQL/etc.
