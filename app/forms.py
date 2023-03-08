from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User
class RegistrationForm(FlaskForm):
    username= StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email= StringField('Email', validators=[DataRequired(), Email()])

    Password= PasswordField('Password', validators=[DataRequired()])
    confirm_Password= PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('Password')])
    submit= SubmitField('Sign up')

    def validate_username(self, username):
        user=User.query.filter_by(username= username.data).first()
        if user:
            raise ValidationError('That Username is taken, Please choose a different one')


    def validate_email(self, email):
        user=User.query.filter_by(email= email.data).first()
        if user:
            raise ValidationError('That Email is taken, Please choose a different one')


class LoginForm(FlaskForm):
    email= StringField('Email', validators=[DataRequired(), Email()])
    Password= PasswordField('Password', validators=[DataRequired()])
    remember= BooleanField('Remember Me')
    submit= SubmitField('Login')