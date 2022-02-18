#%%
#import urllib.request
#import urllib.request as req
from urllib \
import request as req
import bs4
html = \
req.urlopen('http://finance.naver.com/')    
bs=bs4.BeautifulSoup(html, 'html.parser')
#제목태그명검색 
print(bs.find('title'))
