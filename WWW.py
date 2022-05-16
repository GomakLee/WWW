#실시간 검색어 크롤링
import requests
from bs4 import BeautifulSoup
url = "https://zum.com/"
response = requests.get(url)
#print(response)
source_text = response.text
'''
soup = BeautifulSoup(source_text, "html.parser")
#print(soup)
#print(type(soup))
only_need = soup.findAll("div.issue_cont new")
print(only_need)
f = open("Text.txt","w", encoding='utf-8')
for i in only_need:
    f.write(i)
f.close()'''
print(response.status_code)