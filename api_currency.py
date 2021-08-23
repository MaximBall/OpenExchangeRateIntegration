import requests
import json
import csv

link = "https://openexchangerates.org/api/latest.json?app_id=9e598bbecffa4d0587ea7965c5dee75d"
response = requests.get(link)
text = response.text
data = json.loads(text)
dict_rates = data["rates"]

with open('currency.txt', 'w') as f:
    json.dump(dict_rates, f, ensure_ascii=False)

with open('currency.csv', 'w', newline='') as csvfile:
    fieldnames = ['currency_name', 'currency']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for currency_name in dict_rates:
        writer.writerow(
            {'currency_name': currency_name, 'currency': dict_rates[currency_name]}
        )
