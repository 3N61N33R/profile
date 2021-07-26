from decouple import config

DEBUG = True
SECRET_KEY = config("SECRET_KEY")
DATABASE = config("DATABASE")
