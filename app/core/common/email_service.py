from flask_mail import Message
from flask import render_template, copy_current_request_context, current_app
from app.core import app, email
import threading
import logging


def send_mail(email_ids, subject, message_text, html_file=None, html_body=None):
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.ERROR, datefmt="%H:%M:%S")
    default_sender = app.config['MAIL_DEFAULT_SENDER']

    @copy_current_request_context
    def sendind_mail(default_sender, email_ids, subject, message_text, html_file=None, html_body=None):
        if html_file:
            html_message = render_template(html_file, **html_body)
            msg = Message(subject,
                          body=message_text,
                          html=html_message,
                          sender=default_sender,
                          recipients=email_ids)
        else:
            msg = Message(subject,
                          body=message_text,
                          sender=default_sender,
                          recipients=email_ids)
        try:
            result = email.send(msg)
            logging.info(result)
        except Exception as err:
            logging.info(err)

    email_process = threading.Thread(target=sendind_mail, args=(default_sender, email_ids, subject, message_text, html_file, html_body))
    email_process.start()

