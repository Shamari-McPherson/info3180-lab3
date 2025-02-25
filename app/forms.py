from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, validators
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
    name = StringField('NAME',
    validators = [InputRequired()])

    # placeholder = "Please enter your e-mail address.",
    email = EmailField('E-MAIL',
    [validators.DataRequired(), 
    validators.Email()])

    subject = StringField('SUBJECT',
    validators = [InputRequired()])

    message = StringField('MESSAGE',
    validators = [InputRequired()])