#실시간 검색어 크롤링
from cgitb import text
import requests
from bs4 import BeautifulSoup
url = "https://zum.com/"
response = requests.get(url)
#print(response)
source_text = response.text

soup = BeautifulSoup(source_text, "html.parser")
#print(soup)
#print(type(soup))

#only_need = soup.select("#app > div.wrap > header > div.gnb_wrap > div.gnb_menu_wrap > div.w_inner > div.issue_wrap > div.issue_cont new >div.list_wrap issue_type")
text = soup.findAll("span","inner_txt")
print(text)
