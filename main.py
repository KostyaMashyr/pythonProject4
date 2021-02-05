import requests
from bs4 import BeautifulSoup

url = 'https://www.olx.ua/hobbi-otdyh-i-sport/sport-otdyh/velo/velosipedy/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
items = soup.find_all('tr', class_='wrap')
for n, i in enumerate(items, start=1):
    itemName = i.find('h3', class_='lheight22 margintop5').text.strip()
    itemPrice = i.find('p', class_='price').text
    itemURL = i.find('a').get('href')
    print(f' {itemName} {itemPrice} {itemURL}')
