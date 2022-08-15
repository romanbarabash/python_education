import requests
from bs4 import BeautifulSoup


def get_currency_rate(in_currency: str, out_currency: str, amount: int = 1):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={amount}'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_='ccOutputRslt').get_text()
    return float(rate[:-4])


print(get_currency_rate('USD', 'AUD'))
