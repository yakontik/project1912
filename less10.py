import requests
from bs4 import BeautifulSoup


# html_doc = """<html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# """

# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.p)
# print(soup.get_text())
def infoBitcoin():
    response=requests.get("https://coinmarketcap.com/")
    if response.status_code==200:
        response_text=response.text
        soup=BeautifulSoup(response_text,"html.parser")
        #  <a href="/currencies/bitcoin/markets/" class="cmc-link"><span>$23,638.19</span></a>
        soup_list=soup.find_all("a",{"href":"/currencies/bitcoin/markets/"})
        print(soup_list)
        res=soup_list[0].find("span")
        print(res)
        print(f'1 bitcoin = {res.text}')

# infoBitcoin()

def pogodaInRivne():
    url="https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%80%D1%96%D0%B2%D0%BD%D0%B5"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    #<p class="today-temp">+4°C</p>
    temp_now=soup.find("p",class_="today-temp")
    # print(temp_now)
    # print(temp_now.get_text())
    return temp_now.get_text()

result=pogodaInRivne()
print(f'Today in Rivne {result}')

