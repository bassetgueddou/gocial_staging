from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeLocalField, SubmitField
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
    title = StringField("Titre", validators=[DataRequired()])
    description = TextAreaField("Description")
    date = DateTimeLocalField("Date", format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    submit = SubmitField("Valider")

# TODO: add validation for events symbs (à checker le design de eleonor avant de le faire)