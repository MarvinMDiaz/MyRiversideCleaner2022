from flask import Flask
from flask_mail import Mail, Message
import os
import email
import emails
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





app = Flask(__name__)



app.secret_key = os.environ.get("SECRET_KEY")

