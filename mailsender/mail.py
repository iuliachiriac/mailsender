from flask.ext.mail import Mail, Message
from flask import current_app as app, render_template


class MailSender(object):
    mail = Mail()

    def __init__(self, participants):
        MailSender.mail.init_app(app)
        self.participants = participants

    def send_mails(self):
        for score, students in self.participants.iteritems():
            if score not in app.config.get('SCORE_HTML_MAPPING'):
                continue
            for name, email in students:
                msg = self.compose_mail(email, name, score)
                MailSender.mail.send(msg)
                print 'Mail sent to {0} ({1})'.format(email, name)

    def compose_mail(self, recipient, name,  score):
        html = render_template(app.config.get('SCORE_HTML_MAPPING')[score],
                               name=name.decode('utf-8', 'replace'))
        return Message(
            subject=app.config.get('SUBJECT'),
            recipients=[recipient],
            sender=(app.config.get('SENDER'), app.config.get('MAIL_USERNAME')),
            html=html,
        )
