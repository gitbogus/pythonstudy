import requests

url = "http://www.python.org"
resp = requests.get(url)
print(resp)  # 정상을 뜻하는 응답코드

url2 = "https://www.python.org/1"
resp2 = requests.get(url2)
print(resp2) # 해당 페이지를 찾을수 없다는 응답코드

