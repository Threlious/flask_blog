import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = os.getenv('SECRET_KEY')

    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
