from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import pandas as pd
from xml.etree import ElementTree

skey = 'Al5dwUCfM5vQOBl8Lx7R8Jl4Wr5T0jFyWCaGZ7vxjE4s4svNU%2FZU1DFJQLS%2Fya%2F7S6I1xoYUr%2Fnl%2FYrCFczpLg%3D%3D'

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth'
params = '?' + 'ServiceKey=' + skey + '&' + \
urlencode({ quote_plus('returnType') : 'xml', quote_plus('numOfRows') : '100',
            quote_plus('pageNo') : '1'})#, quote_plus('stationName') : '종로구', 
            #quote_plus('dataTerm') : 'DAILY', quote_plus('ver') : '1.0' })
print(url + params)

# query = url + params
# # print(query)
# queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10' })

request = Request(url + params)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
# print(response_body)

root = ElementTree.fromstring(response_body)

df = pd.DataFrame()
for item in root.iter('item'):
    item_dict = {}
    item_dict['addr'] = item.find('addr')
    item_dict['stationName'] = item.find('stationName')
    # item_dict['pm10Value'] = item.find('pm10Value')
    
    df = df.append(item_dict, ignore_index = True)

df
