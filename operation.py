from datetime import datetime


class Operation:

    def __init__(self, date, amount, description, opr_from, opr_to):

        self.date = date
        self.amount = amount
        self.description = description
        self.opr_from = opr_from
        self.opr_to = opr_to

    def __repr__(self):

        return (f"Дата:{self.date}\nСумма и валюта:{self.amount}\n"
                f"Тип перевода:{self.description}\nОткуда:{self.opr_from} > Куда: {self.opr_to}")

    def __str__(self):

        return (f'{self.date_operation()} {self.description_operation()}\n{self.from_operation()}'
                f'{self.to_operation()}\n{self.amount_operation()}\n')

    def date_operation(self):
        """ Возвращает дату в формате '01.01.2001' """

        date = datetime.fromisoformat(self.date)
        return date.strftime('%d.%m.%Y')

    def amount_operation(self):
        """ Возвращает сумму опреации и код валюты """

        return f'{self.amount["amount"]} {self.amount["currency"]["name"]}'

    def description_operation(self):
        """ Возвращает тип операции """

        return self.description

    def from_operation(self):
        """ Возвращает, откуда была выполнена операция"""

        return self.opr_from

    def to_operation(self):
        """ Возвращает, куда была выполнена операция"""

        return self.opr_to
