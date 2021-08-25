import csv
from functools import lru_cache
import time


def get_currency(currency):
    with open('currency.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        need_currency = {
            row['currency_name']: row['currency']
            for row in reader
            if row['currency_name'] == currency
        }
    return need_currency


def all_currencies():
    with open('currency.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        currencies = {
            row['currency_name']: row['currency']
            for row in reader
        }
    return currencies


if __name__ == "__main__":

    currencies = all_currencies()
    print(currencies)

    # currency = input("Input currency name - ")
    # value_currency = get_currency(currency)

