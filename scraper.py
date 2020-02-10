import requests
from bs4 import BeautifulSoup
import numpy as np
import urllib.request


url = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
resp = requests.get(url)

soup = BeautifulSoup(resp.content, features="xml")

items = soup.findAll('item')

news_items = []

for item in items:
    news_item = {}
    news_item['title'] = item.title.text
    news_item['description'] = item.description.text
    news_item['link'] = item.link.text
    news_items.append(news_item)
files = ['file1.txt', 'file2.txt', 'file3.txt','file4.txt', 'file5.txt', 'file6.txt','file7.txt', 'file8.txt', 'file9.txt','file10.txt', 'file11.txt', 'file12.txt','file13.txt', 'file14.txt', 'file15.txt','file16.txt', 'file17.txt', 'file18.txt','file19.txt', 'file20.txt']
for i in range(0,len(news_items)):
    text_file = open(files[i], "w")
    text_file.write(news_items[i]['title'] + '\n')
    text_file.write(news_items[i]['description'] + '\n')
    urllib.request.urlretrieve(news_items[i]['link'])
    url1 = news_items[i]['link']
    r1 = requests.get(url1)
    coverpage = r1.content
    soup1 = BeautifulSoup(coverpage, 'lxml')
    coverpage_news = soup1.find_all('p', class_='css-exrw3m evys1bk0')
    final = ''
    soup = BeautifulSoup(coverpage).find_all('p', class_='css-exrw3m evys1bk0')
    for j in range(0,len(soup)):
        final = final + soup[j].get_text()
    text_file.write(final)
    text_file.close()
