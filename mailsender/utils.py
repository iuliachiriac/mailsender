# encoding: utf-8
from csv import DictReader


SCORE = 'Scor'
NAME = 'Nume și prenume'
MAIL = 'Adresa e-mail'


def get_participants(csv_filename):
    result = {}
    with open(csv_filename, 'rb') as csv_file:
        reader = DictReader(csv_file)
        for row in reader:
            result.setdefault(row[SCORE], []).append((row[NAME], row[MAIL]))
    return result
