from flask import render_template,request,redirect,session, Flask
from flask_app import app
from flask import flash
import smtplib
from flask_app.models.user import User
from flask_mail import Mail, Message
import os
from datetime import datetime
mail = Mail(app)

@app.route('/')
def root():
    return redirect('/cleaning-service/home')

@app.route('/cleaning-service/home')
def home():


    return render_template('home.html', now=datetime.utcnow())

@app.template_filter('dateFormat')
def  datetimeFormat(value, format='%Y'):
    return value.strftime(format)

@app.route("/cleaning-service/contact/submitted", methods=["POST"])
def contactForm():
    if not User.validate_form(request.form):
        print("Failed Validation")
        return redirect("/cleaning-service/home#Contact-Us")
    else:
        print("Grabbing Form Details")
        name= request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        print("Form Info Grabbed")

        msg= Message(subject=f" New Mail from:  '{email}'", body=f"\n\nClients Name: {name}\n\n Email: {email}\n\nPhone Number:{phone}\n\n\nMessage: {message}", sender="diazm.webdev@gmail.com", recipients=["support@myriversidecleaner.com"] )

        print("form formatted")

        print(msg)
        mail.send(msg)

        flash("Message was Succesfully sent ", "success")

        print("Message was Succesfully sent ")


    return redirect("/cleaning-service/home#Contact-Us")








