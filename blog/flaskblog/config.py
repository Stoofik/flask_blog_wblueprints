import os

class Config:
    SECRET_KEY = os.environ.get("KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("URI")
    MAIL_SERVER = "smpt.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True