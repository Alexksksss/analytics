#site - https://www.gctc.ru/main.php?id=98.1
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


url = 'https://www.gctc.ru/main.php?id=98.{}'
session = requests.session()
session.headers = {
  'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
  "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
}

page = 1
try:
  final_l = []

  while page <= 12:
    l = []
    res = session.get(url.format(page))
    page +=1
    res.raise_for_status()
    html = res.text

    soup = BeautifulSoup(html, 'html5lib')
    info = soup.select("div.news")

    l=[]
    for dates in info:
      h2 = dates.select('h2')
      for h2s in h2:
        year = str(h2s.text)[:-3]

        h1 = h2s.find_previous('h1')

        day = int(str(h1.select('b'))[4:6])

        month = h1.select_one('b span').text

        l.append(str(day) + ' ' + month + ' ' + year)
    #print(l)
    final_l += l
  print(final_l)

except HTTPError as ht:
  print(f"ERROR: {ht}")
except Exception as ex:
  print(f"ERROR: {ex}")