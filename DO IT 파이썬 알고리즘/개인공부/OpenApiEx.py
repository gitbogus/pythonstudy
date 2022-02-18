import requests

skey = '%2FbRdqRkfVU8yLWkBHX138t4N7DHh21ldUPJFJZwemDpcfZxwHxa9o1xLGQ8XMUE9DbpNZxs6FBsnxVochSHtFQ%3D%3D'
url = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getMsrstnList'
params ={'serviceKey' : skey, 
         'returnType' : 'xml', 
         'numOfRows' : '100', 
         'pageNo' : '1', 
         'addr' : '서울', 
         'stationName' : '종로구' }

response = requests.get(url, params=params)
print(response.content)

print(input("입력하세요 :"))