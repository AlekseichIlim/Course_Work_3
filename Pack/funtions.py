from operation import Operation
import json


def get_list_sorted(file_operations, count_operations):
    """ Возвращает список, введеного количества, последних операций 'EXECUTED',
        отсортированных по дате """

    with open(file_operations) as file:
        list_opr = []
        list_all_opr = json.load(file)
        for opr in list_all_opr:
            [list_opr.append(opr) for val in opr.values() if val == 'EXECUTED']

    list_opr.sort(key=lambda coll: coll['date'], reverse=True)
    list_opr[count_operations:] = []
    return list_opr


def get_value_from(coll):
    """ Проверяет наличие ключа 'from' и если он есть, возвращает его значение,
        если же его нет возвращает '' """

    if 'from' not in coll:
        return ''
    else:
        return f'{get_account_or_card(coll["from"])} -> '


def get_account_or_card(value_key):
    """ Возвращает зашифрованный номер, в зависимости от того, счет это или карта """

    if 'Счет' in value_key:
        return 'Счет' + ' **' + value_key[-4:]
    else:
        return value_key[:-12] + ' ' + value_key[-12:-10] + '** **** ' + value_key[-4:]


def main(operations_list, count):
    """ Выполняет создание и вывод экземпляров класса Operation """

    for opr in get_list_sorted(operations_list, count):
        opr = Operation(opr['date'], opr['operationAmount'], opr['description'], get_value_from(opr),
                        get_account_or_card(opr['to']))
        print(opr)
