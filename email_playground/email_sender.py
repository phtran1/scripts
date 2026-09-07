import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Myself'
email['to'] = 'testin2@example.com'
email['subject'] = 'Email from Python test'

email.set_content('I am a Python app!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('example@gmail.com', 'your_password')
    smtp.send_message(email)
    print('Email sent successfully!')