import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Myself'
email['to'] = 'testin2@example.com'
email['subject'] = 'Email from Python test'

email.set_content(html.substitute({'name':'Jin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # Note: Gmail no longer allows regular account passwords for SMTP login.
    # You need to generate an "App Password" from Google Account 
    # (navigate to https://myaccount.google.com/apppasswords).
    smtp.login('example@gmail.com', 'your_password')
    smtp.send_message(email)
    print('Email sent successfully!')