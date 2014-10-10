from flask.ext.script import Manager, Command, Option

from mailsender.utils import get_participants
from mailsender.mail import MailSender


def create_manager(app):
    manager = Manager(app)
    manager.add_command('send_mails', SendMails())

    return manager


class SendMails(Command):

    option_list = (
        Option('--csv_file', '-f', dest='csv_file'),
    )

    def run(self, csv_file):
        participants = get_participants(csv_file)
        mail_sender = MailSender(participants)
        mail_sender.send_mails()
