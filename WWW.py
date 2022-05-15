#실시간 검색어 크롤링
import requests

url = "https://zum.com/"
response = requests.get(url)
print(response)
#print(response.text)
response_text = response.text


f = open("Text.txt","w", encoding='utf-8')

f.write(response_text)
f.close()