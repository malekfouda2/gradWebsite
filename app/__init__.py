from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app= Flask(__name__)
app.app_context()
app.config['SECRET_KEY']='0c825127ca0d91cbecb21e4c68dfafe3'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db= SQLAlchemy(app)
app.app_context().push()

bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'
from app import routes