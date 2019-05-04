from random import randint
from time import strftime
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_wtf.recaptcha import RecaptchaField
from config import SECRET_KEY, RECAPTCHA_PUBLIC_KEY, RECAPTCHA_PRIVATE_KEY

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['RECAPTCHA_PUBLIC_KEY'] = RECAPTCHA_PUBLIC_KEY
app.config['RECAPTCHA_PRIVATE_KEY'] = RECAPTCHA_PRIVATE_KEY
print("keys: {} {} {}".format(SECRET_KEY, RECAPTCHA_PUBLIC_KEY, RECAPTCHA_PRIVATE_KEY))

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
