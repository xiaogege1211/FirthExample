#!/usr/bin/python

import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os

# My module for getting a random cat picture
from random_pic import getRandomPic
from random_pic import getRandomCat
from random_pic import getRandomLeague

gmail_user = input("Your gmail address:")
gmail_pwd = getpass.getpass()

receiver = "firthk@limestone.on.ca"
title = "Hello World!"
message = "HAL 9000"
#attachment = "cat.jpg"
#attachment = getRandomCat()
attachment = getRandomPic("\\league")

def mail(to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   encoders.encode_base64(part)
   part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   mailServer.close()

mail(receiver,
     title,
     message,
     attachment)
