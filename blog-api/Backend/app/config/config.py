import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    APP_NAME=os.getenv("APP_NAME" , "Blog-API")
    SECRET_KEY = os.getenv("SECRET_KEY")


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False