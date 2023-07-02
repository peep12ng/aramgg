import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://aramgg:aramggdb1234@192.1:3306/aramgg'
SQLALCHEMY_TRACK_MODIFICATIONS = False