#!/usr/bin/env python3
# Envio dos Logs de backup utilizando a lib smtplib e o smtp do google
# Rafael Monteiro - 20/06/2023

import os
import smtplib
from email.message import EmailMessage
from secret import passwd

# Configurando o e-mail e senha
EMAIL_ADDRESS = 'alerta-backup@gmail.com'
EMAIL_PASSWORD = passwd
EMAIL_LIST = 'youremail1@gmail.com.br youremail2@gmail.com.br tecnologia@gmail.com.br'

# Criando o e-mail
with open('/home/automation/email-python/bkponline') as fp:
    msg = EmailMessage()
    msg.set_content(fp.read())

msg['Subject'] = 'Backup Log ACME - dbserver01'
msg['From'] = EMAIL_ADDRESS
msg['TO'] = EMAIL_LIST

# Enviando o e-mail
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
