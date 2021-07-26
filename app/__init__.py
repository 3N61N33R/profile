# file to initialize a python module
import os
from flask import Flask

# initialize the app
# set instance_relative_config to true to enable loading of the
# config file with app.config.from_object('config')

app = Flask(__name__, instance_relative_config=True)

# load the views
from app.views import hello

# load the config file
app.config.from_object("config")
