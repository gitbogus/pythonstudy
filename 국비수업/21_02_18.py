import requests
import json

url = 'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt=20120101'
resp = requests.get(url)
result = resp.json()
print(result)

num = len(result['boxOfficeResult']['daiLyBoxOfficeList'])
print(num)

result = ['boxOfficeResult']['daiLyBoxOfficeList'][0]['movieNm']
result = ['boxOfficeResult']['daiLyBoxOfficeList'][0]['movieCd']
result = ['boxOfficeResult']['daiLyBoxOfficeList'][0]['openDt']
result = ['boxOfficeResult']['daiLyBoxOfficeList'][0]['audiAcc']

for i in range(0, num):
    print(result = ['boxOfficeResult']['daiLyBoxOfficeList'][0]['movieNm'])
    print(result = ['boxOfficeResult']['daiLyBoxOfficeList'][0]['movieCd'])
    print(result = ['boxOfficeResult']['daiLyBoxOfficeList'][0]['openDt'])
    print(result = ['boxOfficeResult']['daiLyBoxOfficeList'][0]['audiAcc'])