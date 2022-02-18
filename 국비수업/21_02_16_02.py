from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome('chromedriver')
driver.get("http://python.org")
print(driver.current_url)#창주소
print(driver.title)#창제목

#webelement 
menus = driver.find_elements_by_css_selector('#top ul.menu li') 
pypi = None
for m in menus:
    if m.text == "PyPI":
        pypi = m #webelement
    print(m.text)
#https://pypi.python.org/ 이동 
pypi.click()  # 클릭
# <input id="id-search-field" name="q" 검색창 name으로 검색하기
# 태그 name속성으로 특정한 요소를 찾을 수 있음
elem = driver.find_element_by_name("q")

# input 텍스트 초기화 
#elem.clear()
# 키 이벤트 전송가능함
# 태그가 input 태그이므로 입력창에 키이벤트가 전달되면,
#입력값이 자동으로 작성됨
elem.send_keys("list")

# 태그가 input 태그이므로 엔터 입력시 form action이 진행됨
elem.send_keys(Keys.RETURN)

# 스크린샷 파일생성
driver.set_window_size(1400, 1000)
driver.get_screenshot_as_file("screenshot.png")

# 프로젝트 이름 검색
# 최초 발견한 태그만 검색
title = driver.find_element_by_tag_name('h3')

print (title.text) #list1 1.0.0
# 모든 태그 검색
h3s = driver.find_elements_by_tag_name('h3')
print (h3s[0].text)#List 1.3.0

for h3 in h3s:
    print (h3.text)
