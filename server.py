from flask import Flask, render_template, request, redirect
from form import SurveyForm
from mysqlconnection import connectToMySQL

app = Flask('__name__')

app.secret_key = "development_key"

@app.route("/index", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def index():
    form = SurveyForm()
    return render_template("index.html", form=form)
        
@app.route("/save_survey", methods=['POST'])
def save_survey():
    form = SurveyForm()
    if form.validate == False:
        return render_template("index.html", form=form)
    else:
        my_sql = connectToMySQL('flask_pets')
        query = "INSERT INTO dojo_survey(name, gender, location, language, comment, created_at) VALUES(%(name)s, %(gender)s, %(location)s, %(language)s, %(comment)s, NOW())"
        data = {
            "name": form.name.data,
            "gender": form.gender.data,
            "location": form.location.data,
            "language":  form.language.data,
            "comment": form.comment.data
        }
        id = my_sql.query_db(query, data)
        return redirect("/survey_detail/"+str(id))

@app.route("/survey_detail/<id>")
def survey_detail(id):
    my_sql = connectToMySQL('flask_pets')
    query = "SELECT sur.id, sur.name, sur.gender, lan.name as language, loc.name as location, sur.comment FROM languages lan join dojo_survey sur on sur.language = lan.id join locations loc on sur.location = loc.id WHERE sur.id = %(id)s"
    data = {
        "id": id
    }
    surveyInfo = my_sql.query_db(query, data)
    return render_template("/detail.html", surveyInfo=surveyInfo)

if __name__ == '__main__':
    app.run(debug=True)