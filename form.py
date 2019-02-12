from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Length
from mysqlconnection import connectToMySQL

def getLocationList():
    my_sql = connectToMySQL('flask_pets')
    return my_sql.query_db("select * from locations")

def getLanguageList():
    my_sql = connectToMySQL('flask_pets')
    return my_sql.query_db("select * from languages")

class SurveyForm(Form):
    name = StringField('Your Name: ', validators=[DataRequired("Please enter your name")])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female'), ('NN', 'Dont Need to answer')], validators=[DataRequired("Gender is required")])
    
    # >>>> to create dynamic choice list for SelectedField <<<< #
    locList = getLocationList()
    locOptions = [('', '')]    
    for loc in locList:        
        locOptions.append((loc['id'] , loc['name']))
    # >>>> to create dynamic choice list for SelectedField <<<< #    
    location = SelectField('Dojo Location: ', choices=locOptions, validators=[DataRequired("Please select the location")])
    
    # >>>> to create dynamic choice list for SelectedField <<<< #
    lanList = getLanguageList()
    lanOptions = [('', '')]    
    for lan in lanList:        
        lanOptions.append((lan['id'] , lan['name']))
    # >>>> to create dynamic choice list for SelectedField <<<< #
    language = SelectField('Favourite Language: ', choices=lanOptions, validators=[DataRequired("Please select language")])
    
    comment = TextAreaField('Comment (Optional): ', validators=[Length(max=120, message="The comment should be less than 120 characters")])
    submit = SubmitField('Submit')