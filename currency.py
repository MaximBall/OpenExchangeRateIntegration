import json
import csv
from functools import lru_cache
import time

# with open("currency.txt", "r") as f:
#     data = json.load(f)
# print(data[currency])


@lru_cache(maxsize=256)
def get_currency(currency):
    with open('currency.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        need_currency = {
            row['currency_name']: row['currency']
            for row in reader
            if row['currency_name'] == currency
        }
    return need_currency


currency = input("Input currency name - ")
start = time.time()
value_currency = get_currency(currency)
end = time.time()
print(value_currency, start, end)

start = time.time()
value_currency = get_currency(currency)
end = time.time()
print(value_currency, start, end)
