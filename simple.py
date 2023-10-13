#爬表特版圖片
#requests module送http request
import requests
#BeautifulSoup module分析html
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Beauty/M.1696977017.A.248.html'
d = {"over18" : '1'} #夾帶滿18的參數送request 
r = requests.post(url,cookies=d)
soup = BeautifulSoup(r.text,'html.parser') #use html.parser parse html
img = soup.find_all('img') #用find_all function 篩選

for link in img:
  print(link.get('src')) #得到src的內容(圖片)
