import requests
from bs4 import BeautifulSoup
from urlextract import URLExtract
import urllib.request
import os, os.path

if os.path.exists("stiker download") == False:
	os.mkdir("stiker download")

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0', 'accept': '*/*'}
extractor = URLExtract()
url = input("Отправьте ссылку: ")
#https://store.line.me/emojishop/product/60f7bab1b99b030cdf726120/en


def get_html(url, params=None):
	r = requests.get(url, headers=HEADERS, params=params)
	r.encoding = 'UTF-8'
	print(r)
	return r

html = get_html(url)

soup = BeautifulSoup(html.text, 'html.parser')

main_block = soup.find('div',  {"data-widget": "StickerPreview", "data-widget-id": "StickerPreview"})

items = main_block.find_all('span')

pattern = r"(?<=url\().*(?='\))"

items = items[::2]

number_file = 0

def changeCar(ch,ca1,ca2):
    b = ''
    for x in ch:
        if x!= ca1:
            b+= x
        else:
            b+=ca2
    return b

url_file = soup.find('p', {"data-test": "emoji-name-title"}).text
url_file = changeCar(url_file, ".", "")
url_file = changeCar(url_file, "/", "")
url_file = changeCar(url_file, "-", "")

if os.path.exists(f"stiker download/{url_file}") == False:
	os.mkdir(f"stiker download/{url_file}")

for item in items:
	style = item['style']
	for url2 in extractor.gen_urls(style):

		print (url2)
		urllib.request.urlretrieve(url2, f"stiker download/{url_file}/{number_file}.jpg")
		
		number_file += 1
