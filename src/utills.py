# -*- coding: utf-8 -*-

from load_json import date_correction, sorting

date_cor = date_correction()

def get_five_operations():
    return sorting(date_cor)[-5:]

def reversed_operation_five():
    r_operation_five = get_five_operations()
    r_operation_five.reverse()
    return r_operation_five

def hide_symbols():
    five_operations = reversed_operation_five()

    for element in five_operations:
        if element['to'][0] == 'С':
            element['to'] ='Счет ' + '**' + element['to'][-4:]
        else:
            element['to'] = element['to'][:-12] + ' ' + element['to'][-11:-9] + '** ' + '**** ' + element['to'][-4:]
        if 'from' in element:
            if element['from'][0] == 'С':
                element['from'] = 'Счет ' + '**' + element['from'][-4:]
            else:
                element['from'] = element['from'][:-12] + ' ' + element['from'][-11:-9] + '** ' + '**** ' + element['from'][-4:]
        else:
            continue


    return five_operations


