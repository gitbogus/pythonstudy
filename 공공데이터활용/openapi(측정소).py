from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import pandas as pd
import json

def baro_api(skey, res_id, encode):
    stype = 'json'
    url = 'http://apis.data.go.kr/1130000/SbcnRspnStatService'
    params = f'?ServiceKey={skey}&&type={stype}&resId={res_id}&' + encode
    query = url + params
# print(query)
    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10' })

    request = Request(query)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
# print(response_body)

    response_dict = json.loads(response_body.decode('utf-8'))
    items = response_dict['statsYr']['indutyNm']

    df = pd.DataFrame(items)
    return df


## 지정 상권 조회
skey = 'Al5dwUCfM5vQOBl8Lx7R8Jl4Wr5T0jFyWCaGZ7vxjE4s4svNU%2FZU1DFJQLS%2Fya%2F7S6I1xoYUr%2Fnl%2FYrCFczpLg%3D%3D'
res_id = 'storezone'
encode = urlencode({quote_plus('key') : '573'}) 
baro_api(skey, res_id, encode)