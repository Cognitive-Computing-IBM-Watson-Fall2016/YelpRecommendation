from flask import Flask

app = Flask(__name__, static_url_path='')

app.secret_key = 'pj_app development key'

#import pj_app.models
#import nd_app.forms
import pj_app.routes


