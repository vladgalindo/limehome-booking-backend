from flask_mail import Message
from flask import render_template
from app import app, email


def send_mail(email_ids, subject, message_text, html_file=None, html_body=None):
    if html_file:
        html_message = render_template(html_file, **html_body)
        msg = Message(subject,
                      body=message_text,
                      html=html_message,
                      sender=app.config['MAIL_DEFAULT_SENDER'],
                      recipients=email_ids)
    else:
        msg = Message(subject,
                      body=message_text,
                      sender=app.config['MAIL_DEFAULT_SENDER'],
                      recipients=email_ids)

    email.send(msg)

