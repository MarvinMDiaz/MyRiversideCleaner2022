from flask import render_template,request,redirect,session, Flask
from flask_app import app
from flask import flash
from flask_app.models.user import User
from flask_mail import Mail, Message
import os
from datetime import datetime
# EMAIL SENDING IMPORTS #
import email
import emails
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




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
        name= request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        msg = request.form['message']

        message = emails.html(

            html =  f"<br>Clients Name:{name}<br>"
                    f"Email: {email}<br>"
                    f"Phone Number:{phone}<br>"
                    f"Message: {msg}<br>",
            subject = f"New email from Website<br>",
            mail_from = os.environ.get("mail_username2")

    )

        message.send(
            to = os.environ.get("mail_username"),
            smtp = {
                "host": "email-smtp.us-east-1.amazonaws.com",
                "port": 587, 
                "timeout": 5,
                "user": os.environ.get("SMTP_Username"),
                "password": os.environ.get("SMTP_Password"),
                "tls": True,
            }
        )


        flash("Message was Succesfully sent ", "success")

        print("Message was Succesfully sent ")


    return redirect("/cleaning-service/home#Contact-Us")








