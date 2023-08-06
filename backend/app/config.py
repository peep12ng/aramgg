import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:7120@db/aramgg'
SQLALCHEMY_TRACK_MODIFICATIONS = False