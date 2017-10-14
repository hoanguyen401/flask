import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from wsgiref.util import application_uri

BASE_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder='/home/behien/eclipse-workspace/Flask/survey')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root''' + '@localhost/test'
db = SQLAlchemy(app)

 