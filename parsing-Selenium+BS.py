# copy info from https://www.nbcomputers.ru/catalog/noutbuki/ to csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import random
import time
import csv

service = Service(executable_path='/usr/lib/chromium-browser/chromedriver')
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=service)


try:
    driver.get("https://www.nbcomputers.ru/catalog/noutbuki/")
    driver.implicitly_wait(10)
    button = driver.find_element(By.CSS_SELECTOR, "button.sc-47746e2f-0")
    actions = ActionChains(driver)
    actions.move_to_element(button)
    actions.perform()
    wait = WebDriverWait(driver, timeout=5)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sc-47746e2f-0"))).click()
    while True:
       wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sc-47746e2f-0"))).click()
       time.sleep(random.random())

except Exception as ex:
    print(f'Error: {ex}')

html = driver.page_source
#print(html)
driver.quit()


soup = BeautifulSoup(html,'lxml')
#print(soup.encode('utf-8'))

l = []
cards = soup.select_one('div.sc-26679455-1')
for card in cards:

    name = card.select_one('h2.sc-d9406361-0')
    if name:
        name = name.text
    else:
        name = ''
    #print('name=',name)

    price = card.select_one('span.sc-96470d6e-2')
    if price:
        price = price.text
    else:
        price = ''
    #print('price=', price.encode('utf-8'))

    code = card.select_one('p.sc-d9406361-0')
    if code:
        code = code.text[5:]
    else:
        code = ''
    #print('code=',code)

    l.append({
        'name': str(name.encode('ascii','ignore')).replace('b','').replace("'",''),
        'price': int(str(price.encode('ascii','ignore')).replace('b','').replace("'",'')),
        'code': code
    })

print(l)
with open('task2(selenium+Bs).csv', 'w') as f:
  writer = csv.DictWriter(f, l[0].keys())
  writer.writeheader()
  for row in l:
    writer.writerow(row)