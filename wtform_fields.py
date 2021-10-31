from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from models import User
from passlib.hash import pbkdf2_sha256

def invalid_credentials(form, field):
    """ Username and Password checker """
    username_entered = form.username.data
    password_entered = field.data
    user_object = User.query.filter_by(username=username_entered).first()
    if user_object is None:
        raise ValidationError("Oops! The username or password is incorrect!")
    elif not pbkdf2_sha256.verify(password_entered, user_object.password):
        raise ValidationError("Oops! The username or password is incorrect!")
class RegistrationForm(FlaskForm):
    """ Registration form """
    username = StringField('username_label', validators=[InputRequired(message="Oops! You need to make a username!"), Length(min=4, message="Oops! You muust have at least 4 characters in your username!")])
    password = PasswordField('password_label', validators=[InputRequired(message="Oops! You need to make a password!"), Length(min=8, message="Oops! You muust have at least 8 characters in your password!")])
    confirm_pswd = PasswordField('confirm_pswd_label', validators=[InputRequired(message="Oops! You need to confirm your password!"), EqualTo('password', message="Oops! Your passwords must match!")])
    submit_button = SubmitField('Create')
    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Oops! This username already exists! Make a new one.")
class LoginForm(FlaskForm):
    """ Login Form """
    username = StringField('username_label', validators=[InputRequired(message="Oops! Username is required!")])
    password = PasswordField('password_label', validators=[InputRequired(message="Oops! Password is required!"), invalid_credentials])
    submit_button = SubmitField('Log in')
