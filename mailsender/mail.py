from flaskext.mail import Mail, Message
from flask import current_app as app, render_template


SCORE_HTML_MAPPING = {
    '0': 'other_universities.html',
}


class MailSender(object):
    mail = Mail()

    def __init__(self, participants):
        MailSender.mail.init_app(app)
        self.participants = participants

    def send_mails(self):
        for score, students in self.participants.iteritems():
            for name, email in students:
                msg = self.compose_mail(email, name, score)
                MailSender.mail.send(msg)

    def compose_mail(self, recipient, name,  score):
        html = render_template(SCORE_HTML_MAPPING[score], name=name)
        return Message(
            subject=app.config.get('SUBJECT'),
            recipients=[recipient],
            sender=(app.config.get('SENDER'), app.config.get('MAIL_USERNAME')),
            html=html,
        )
