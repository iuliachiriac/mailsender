from flask.ext.script import Manager, Command, Option


def create_manager(app):
    manager = Manager(app)
    manager.add_command('send_mails', MailSender())

    return manager


class MailSender(Command):

    option_list = (
        Option('--csv_file', '-f', dest='csv_file'),
    )

    def run(self, csv_file):
        print csv_file
