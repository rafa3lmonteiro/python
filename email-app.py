import os
import smtplib
from email.message import EmailMessage
from segredos import senha

# Configurar e-mail, senha
EMAIL_ADDRESS = 'my@gmail.com'
EMAIL_PASSWORD = senha

# Criar um e-mail
msg = EmailMessage()
msg['Subject'] = 'Backup #37 realizado com sucesso'
msg['From'] = 'my@gmail.com'
msg['TO'] = 'your@gmail.com'
msg.set_content('O Backup do Banco foi realizado com sucesso')

# Enviar um e-mail
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
