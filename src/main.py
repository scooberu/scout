from random import randint
from time import strftime
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, RecaptchaField

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'e657d3949722c1c3473c5704fd025f1d'

RECAPTCHA_PUBLIC_KEY = "6Ld9yaEUAAAAAPOZ_ivD9Mwk85YdCmMyjRI_RxKC"
RECAPTCHA_PRIVATE_KEY = "6Ld9yaEUAAAAAM5-vlSEfi913hKlTlTj58GslEkq"


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    surname = TextField('Surname:', validators=[validators.required()])
    recaptcha = RecaptchaField()

def get_time():
    time = strftime("%Y-%m-%dT%H:%M")
    return time

# def write_to_disk(name, surname, email):
#     data = open('file.log', 'a')
#     timestamp = get_time()
#     data.write('DateStamp={}, Name={}, Surname={}, Email={} \n'.format(timestamp, name, surname, email))
#     data.close()

@app.route("/", methods=['GET', 'POST'])
def schedule():
    form = ReusableForm(request.form)

    #print(form.errors)
    if request.method == 'POST':
        name=request.form['name']
        surname=request.form['surname']
        email=request.form['email']
        password=request.form['password']

    if form.validate():
        #
        # Do your work here
        #
        flash('Hello: {} {}'.format(name, surname))

    else:
        flash('Error: All Fields are Required')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()