from flaskext.mail import Mail, Message
from flask import current_app as app


class MailSender(object):
    mail = Mail()

    def __init__(self, participants):
        MailSender.mail.init_app(app)
        self.participants = participants

    def send_mails(self):
        pass
