from bs4 import BeautifulSoup
import requests
from functools import lru_cache


headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'})
urls = ["https://inventure.com.ua/tools/database/rejting-top-50-krupnejshie-it-kompanij-v-ukraine",
        "https://inventure.com.ua/analytics/digest",
        "https://inventure.com.ua/investments",
        "https://inventure.com.ua/analytics"
]


@lru_cache(maxsize=256)
def get_companies_list(url):
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup.text


if __name__ == '__main__':
    for url in urls:
        print(get_companies_list(url))
    print("done")
    print()