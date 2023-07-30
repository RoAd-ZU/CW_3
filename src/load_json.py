# -*- coding: utf-8 -*-

import json
from datetime import datetime


def load_json():
    with open('operations.json', 'r', encoding="utf-8") as operations_:
        return json.load(operations_)

def search_for_errors():
    operations = []
    for element in load_json():
        if 'state' in element:
            operations.append(element)
    return operations


def removees_canceled():
    operetion_executed = []
    for element in search_for_errors():
        if element['state'] == 'EXECUTED':
            operetion_executed.append(element)
    return operetion_executed
def date_correction():
    operations = []
    for element in removees_canceled():
        date = datetime.strptime(element['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        element['date'] = date
        operations.append(element)
    return operations

def sorting(date_corr):
    return sorted(date_corr, key=lambda e: '.'.join(reversed(e['date'].split('.'))))

