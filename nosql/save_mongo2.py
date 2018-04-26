from pymongo import MongoClient
from bs4 import BeautifulSoup 
from urllib.request import urlopen

html = urlopen('http://www.yes24.com/Mall/Main/Book/001?CategoryNumber=001')
soup = BeautifulSoup(html, 'html.parser')
b = soup.find_all(class_="rnk_name")
# for x in b:
#     print(x.a.string)
#     print(x.a['href'])
# print("book =", b)

client = MongoClient('localhost', 27017)
db = client.scraping  # scraping 데이터베이스를 추출
collection = db.best  # best 콜렉션을 추출
 
collection.delete_many({})
 
for x in b:
    collection.insert_one({
        'url': x.a['href'],
        'title': x.a.string,
    })
 
for link in collection.find().sort('_id'):
    print(link['_id'], link['url'], link['title'])