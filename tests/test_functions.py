from Pack.functions import get_value_from, get_account_or_card, main


def test_get_value_from_1(operation1_fix):
    assert get_value_from(operation1_fix) == 'Maestro 1596 83** **** 5199 -> '


def test_get_value_from_2(operation2_fix):
    assert get_value_from(operation2_fix) == ''


def test_get_account_or_card_1(value_key_from_1):
    assert get_account_or_card(value_key_from_1) == 'Счет **9589'


def test_get_account_or_card_2(value_key_from_2):
    assert get_account_or_card(value_key_from_2) == 'Maestro 1596 83** **** 5199'


def test_main():
    assert main('data/operations.json', 1) is None
