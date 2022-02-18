from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import pandas as pd
import json

def baro_api(skey, res_id, encode):
    stype = 'json'
    url = 'http://apis.data.go.kr/B553077/api/open/sdsc/baroApi'
    params = f'?ServiceKey={skey}&&type={stype}&resId={res_id}&' + encode
    query = url + params
# print(query)
    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10' })

    request = Request(query)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
# print(response_body)

    response_dict = json.loads(response_body.decode('utf-8'))
    items = response_dict['body']['items']

    df = pd.DataFrame(items)
    return df


## 지정 상권 조회
skey = 'Al5dwUCfM5vQOBl8Lx7R8Jl4Wr5T0jFyWCaGZ7vxjE4s4svNU%2FZU1DFJQLS%2Fya%2F7S6I1xoYUr%2Fnl%2FYrCFczpLg%3D%3D'
res_id = 'storezone'
encode = urlencode({quote_plus('key') : '573'}) 
baro_api(skey, res_id, encode)

## 반경내 상권조회

encode = urlencode({quote_plus('catId') : 'radius', quote_plus('radius') : '500',
                    quote_plus('cx') : '127.004528', quote_plus('cy') : '37.567538'}) 
baro_api(skey, res_id, encode)

# 사각형내 상권조회
encode = urlencode({quote_plus('catId') : 'rectangle', 
                    quote_plus('minx') : '126.978020', quote_plus('miny') : '37.557825',
                    quote_plus('maxx') : '126.987732', quote_plus('maxy') : '37.562022'}) 
baro_api(skey, res_id, encode)

# 행정구역 단위 상권조회(sotreZoneInAdmi) 
encode = urlencode({quote_plus('catId') : 'dong', 
                    quote_plus('divId') : 'adongCd', quote_plus('key') : '1168069000'})
baro_api(skey, res_id, encode)

# 행정동 단위 상가업소 조회(storeListInDong) 
res_id = 'store'
encode = urlencode({quote_plus('catId') : 'dong', 
                    quote_plus('divId') : 'ctprvnCd', quote_plus('key') : '11'})
baro_api(skey, res_id, encode)




