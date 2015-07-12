from flask import Flask, url_for
from flask.ext.sqlalchemy import SQLAlchemy

from renbroc.config import *

import logging

import nltk

app = Flask(__name__, static_url_path='/static')

# Edit database connection below
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ren_user:ren_pass@localhost/renbroc?charset=utf8&use_unicode=1';
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

config = os.getenv('CONFIG_OBJECT', 'LocalConfig')
#print 'loading config:', config
app.config.from_object(eval(config))

db = SQLAlchemy(app)


import renbroc.views, renbroc.models
# from app import views, models


#from api import api

#app.register_blueprint(api, url_prefix='/api')


#from renbroc.admin import renbroc_admin
