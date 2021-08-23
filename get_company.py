from bs4 import BeautifulSoup
import requests
headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'})

url = "https://inventure.com.ua/tools/database/rejting-top-50-krupnejshie-it-kompanij-v-ukraine"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
my_company = soup.find_all("td", attrs={'style': 'font-style: inherit;'})

company_name = [company.text for company in my_company]
print(company_name)
