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
import email.utils
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
        mail = request.form['email']
        phone = request.form['phone']
        msg2 = request.form['message']



        # Replace sender@example.com with your "From" address. 
        # This address must be verified.
        SENDER =os.environ.get("mail_username2")

        SENDERNAME = 'Support Team'

        # Replace recipient@example.com with a "To" address. If your account 
        # is still in the sandbox, this address must be verified.
        RECIPIENT  = os.environ.get("mail_username")

        # Replace smtp_username with your Amazon SES SMTP user name.
        USERNAME_SMTP = os.environ.get("SMTP_Username")


        # Replace smtp_password with your Amazon SES SMTP password.
        PASSWORD_SMTP = os.environ.get("SMTP_Password")

        HOST = "email-smtp.us-east-1.amazonaws.com"
        PORT = 587

        # The subject line of the email.
        SUBJECT = f"New email from Website"

        # The email body for recipients with non-HTML email clients.
        BODY_TEXT =  (

            "\n"
            f"\nClients Name: {name}"
            f"\nEmail: {mail}"
            f"\nPhone Number:{phone}"
            f"\nMessage: {msg2}"

            )

        # The HTML body of the email.
        # BODY_HTML = """<html>
        # <head></head>
        # <body>
        # <h1>Amazon SES SMTP Email Test</h1>
        # <p>This email was sent with Amazon SES using the
        #     <a href='https://www.python.org/'>Python</a>
        #     <a href='https://docs.python.org/3/library/smtplib.html'>
        #     smtplib</a> library.</p>
        # </body>
        # </html>
        #             """

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = SUBJECT
        msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
        msg['To'] = RECIPIENT
        # Comment or delete the next line if you are not using a configuration set
        # msg.add_header('X-SES-CONFIGURATION-SET',CONFIGURATION_SET)

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(BODY_TEXT, 'plain')
        # part2 = MIMEText(BODY_HTML, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        # msg.attach(part2)

        # Try to send the message.
        try:  
            server = smtplib.SMTP(HOST, PORT)
            server.ehlo()
            server.starttls()
            #stmplib docs recommend calling ehlo() before & after starttls()
            server.ehlo()
            server.login(USERNAME_SMTP, PASSWORD_SMTP)
            server.sendmail(SENDER, RECIPIENT, msg.as_string())
            server.close()
        # Display an error message if something goes wrong.
        except Exception as e:
            print ("Error: ", e)
        else:
            print ("Email sent!")














    #     message = emails.html(

    #         html =  f"<br>Clients Name:{name}<br>"
    #                 f"Email: {email}<br>"
    #                 f"Phone Number:{phone}<br>"
    #                 f"Message: {msg}<br>",
    #         subject = f"New email from Website<br>",
    #         mail_from = os.environ.get("mail_username2")

    # )

    #     message.send(
    #         to = os.environ.get("mail_username"),
    #         smtp = {
    #             "host": "email-smtp.us-east-1.amazonaws.com",
    #             "port": 587, 
    #             "timeout": 5,
    #             "user": os.environ.get("SMTP_Username"),
    #             "password": os.environ.get("SMTP_Password"),
    #             "tls": True,
    #         }
    #     )


        flash("Message was Succesfully sent ", "success")

        print("Message was Succesfully sent ")


    return redirect("/cleaning-service/home#Contact-Us")








