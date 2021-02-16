from flask import Flask
from os import path


app = Flask(__name__)
app.config.from_object('config')


from stripdf import views

