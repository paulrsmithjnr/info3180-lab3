from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'passphrase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = 'cc284c4b89c5c6'
app.config['MAIL_PASSWORD'] = 'ac15b593f650ea'
mail = Mail(app)

from app import views
