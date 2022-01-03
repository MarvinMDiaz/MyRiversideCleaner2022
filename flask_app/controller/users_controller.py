from flask import render_template,request,redirect,session, Flask
from flask_app import app
from flask import flash
import smtplib
from flask_app.models.user import User
from flask_mail import Mail, Message
import os
from datetime import datetime


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
            return redirect("/cleaning-service/home#Contact-Us")
        else:
            mail = Mail(app)
            name= request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            message = request.form['message']

            msg= Message(subject=f" New Mail from:  '{email}'", body=f"\n\nClients Name: {name}\n\n Email: {email}\n\nPhone Number:{phone}\n\n\nMessage: {message}", sender=os.environ.get("mail_username"), recipients=["support@myriversidecleaner.com"] )

            mail.send(msg)

            flash("Message was Succesfully sent ", "success")

            print("Message was Succesfully sent ")


        return redirect("/cleaning-service/home#Contact-Us")








