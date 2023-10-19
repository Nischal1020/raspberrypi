import smtplib

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'nexdigo414@gmail.com'
smtp_password = '414@NexDigo12345#'

from_email = 'nexdigo414@gmail.com'
to_email = 'technicalnazwa@gmail.com'
subject = 'Hello, world!'
body = 'This is a test email.'

message = f'Subject: {subject}\n\n{body}'

with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.sendmail(from_email, to_email, message)
