import os
import smtplib
import imghdr
from email.message import EmailMessage


class Mail():
    def __init__(self):
        EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
        EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

        contacts = ['my_email@company.com']

        msg = EmailMessage()
        msg['Subject'] = 'Subject_of_the_mail '
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = contacts

        msg.set_content('This is a plain text email')

        msg.add_alternative("""\
        <!DOCTYPE html>
        <html>
            <body>
                <h4 style = 'color:SlateGray;'> Hi </h4>
                <h4 style="color:SlateGray;">Welcome to the site</h4>
               
            </body>
        </html>
        """, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)


m = Mail()
