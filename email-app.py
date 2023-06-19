#!/usr/bin/env python3
import os
import smtplib
from email.message import EmailMessage
from segredos import senha

# Configurar e-mail, senha
EMAIL_ADDRESS = 'my@gmail.com'
EMAIL_PASSWORD = senha

# Criar um e-mail
with open('/home/automation/email-python/bkponline') as fp:
    msg = EmailMessage()
    msg.set_content(fp.read())

msg['Subject'] = 'Backup Log Acme - serverdb'
msg['From'] = EMAIL_ADDRESS
msg['TO'] = 'your@gmail.com'

# Enviar um e-mail
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
