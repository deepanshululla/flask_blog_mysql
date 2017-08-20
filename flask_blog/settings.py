import os
from base64 import b64encode

random_bytes = os.urandom(64)
SECRET_KEY = b64encode(random_bytes).decode('utf-8')
DEBUG = True;

DB_USERNAME = 'root'
DB_PASSWORD = 'test' 
BLOG_DATABASE_NAME = 'mysql'
DB_HOST = 'mysql:3306'
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI;
SQLALCHEMY_TRACK_MODIFICATIONS = True;
UPLOADED_IMAGES_DEST = '/opt/flask_blog/static/images'
UPLOADED_IMAGES_URL = '/static/images/'
