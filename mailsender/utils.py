# encoding: utf-8
from csv import DictReader
from flask import current_app as app


def get_participants(csv_filename):
    score = app.config.get('SCORE_FIELD')
    name = app.config.get('NAME_FIELD')
    mail = app.config.get('EMAIL_FIELD')
    result = {}
    with open(csv_filename, 'rb') as csv_file:
        reader = DictReader(csv_file)
        for row in reader:
            result.setdefault(row[score], []).append((row[name], row[mail]))
    return result
