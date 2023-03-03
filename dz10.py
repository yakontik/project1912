
import requests
from bs4 import BeautifulSoup
'''
url = 'https://sinoptik.ua/'
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
temp_now=soup.find("p",class_="today-temp")
max_temp=soup.find("p",class_="max_temp")
min_temp=soup.find("p",class_="min_temp")


print(temp_now)
print(temp_now.get_text())
print(max_temp)
print(max_temp.get_text())
print(min_temp)
print(min_temp.get_text())
'''

class CurrencyConverter:
    def __init__(self):
        self.url = "https://bank.gov.ua/ua/markets/exchangerates"
        self.rate = self.get_usd_rate()

    def get_usd_rate(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", class_="exchange-rates__table")
        if table is None:
            print("Таблицю курсів валют не знайдено на сторінці")
            return None
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip() == "Долар США":
                rate = float(cells[1].text.strip().replace(",", "."))
                return rate

    def convert_to_usd(self, amount):
        if self.rate is None:
            print("Не вдалося отримати курс долара США")
            return None
        return amount / self.rate

converter = CurrencyConverter()
amount = float(input("Введіть кількість валюти вашої країни: "))
usd_amount = converter.convert_to_usd(amount)
if usd_amount is not None:
    print("Сума в доларах США: {:.2f}".format(usd_amount))