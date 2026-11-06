import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "development-only-key")


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False