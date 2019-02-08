from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField, TextAreaField, RadioField
from wtforms.validators import DataRequired

class SurveyForm(Form):
    name = StringField('Your Name: ', validators=[DataRequired("Please enter your name")])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female'), ('NN', 'Dont Need to answer')], validators=[DataRequired("Gender is required")])
    location = SelectField('Dojo Location: ', choices=[('',''), ('SJ', 'San Jose'), ('WA', 'Washington')], validators=[DataRequired("Please select the location")])
    language = SelectField('Favourite Language: ', choices=[('', ''), ('Py','Python'), ('JS','JavaScript')], validators=[DataRequired("Please select language")])
    comment = TextAreaField('Comment (optional): ')
    submit = SubmitField('Button')