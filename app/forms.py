from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import validators, StringField, TextAreaField, RadioField


class UploadForm(FlaskForm):
    firstname = StringField('First Name',[validators.DataRequired()])
    lastname = StringField('Last Name',[validators.DataRequired()])
    gender = RadioField('Gender', [validators.DataRequired()],choices=[('Male','Male'),('Female','Female')])
    email = StringField('Email',[validators.DataRequired(),validators.Email()])
    location = StringField('Location',[validators.DataRequired()])
    bio = TextAreaField('Biography',[validators.DataRequired()])
    image = FileField('Profile Picture',validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])