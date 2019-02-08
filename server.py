from flask import Flask, render_template, request
from form import SurveyForm

app = Flask('__name__')

app.secret_key = "development_key"

@app.route("/index", methods=['GET', 'POST'])
def index():

    form = SurveyForm()
    
    if request.method == 'GET':
        return render_template("index.html", form=form)
    elif request.method == 'POST':
        if form.validate == False:
            return render_template("index.html", form=form)
        else:
            name = form.name.data
            gender = form.gender.data
            location = form.location.data
            language = form.language.data
            comment = form.comment.data
            return render_template("detail.html", name=name, gender=gender, location=location, language=language, comment=comment)
   

if __name__ == '__main__':
    app.run(debug=True)