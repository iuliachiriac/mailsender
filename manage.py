#!/usr/bin/env python

from mailsender.app import create_app
from mailsender.manager import create_manager

app = create_app()


if __name__ == '__main__':
    create_manager(app).run()
