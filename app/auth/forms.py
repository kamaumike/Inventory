from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email
from ..models import User


class SignUpForm(FlaskForm):
    """
    The Sign Up Form
    """
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self, field):
        """
        Verify if email already exists in the database
        """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(
                'Email is already exists! Use a different email.')


class LoginForm(FlaskForm):
    """
    The Login Form
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
