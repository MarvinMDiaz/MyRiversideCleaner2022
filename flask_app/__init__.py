from flask import Flask
from flask_mail import Mail, Message
import os



app = Flask(__name__)


# app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = "email-smtp.us-east-1.amazonaws.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS']=  True
app.config['MAIL_USE_SSL']= False
app.config['MAIL_DEBUG'] = True
# app.config["MAIL_USERNAME"]= os.environ.get("mail_username")
app.config["MAIL_USERNAME"]= os.environ.get("SMTP_Username")
# app.config["MAIL_PASSWORD"] = os.environ.get("mail_password")
app.config["MAIL_PASSWORD"] = os.environ.get("SMTP_Password")
app.config['MAIL_DEFAULT_SENDER'] = None
app.config['MAIL__MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)




app.secret_key = os.environ.get("SECRET_KEY")

