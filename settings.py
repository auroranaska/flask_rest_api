import os

DB_USER =  os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASS", "pass")
HOST = os.getenv("DB_HOST", "host")
PORT = os.getenv("DB_PORT", "port")
DB_NAME = os.getenv("DB_NAME", "db_name")

SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PASSWORD, HOST, PORT, DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False
BUNDLE_ERRORS = True
SECRET_KEY = "secretkey"