from selenium import webdriver
import time
driver = webdriver.Chrome('chromedriver')
driver.get("http://python.org")
 
menus = driver.find_elements_by_css_selector('#top ul.menu li')
 
pypi = None
for m in menus:
    if m.text == "PyPI":
        pypi = m #PyPI 메뉴 webelement
    print(m.text)
#https://pypi.python.org/ 이동 
pypi.click()  # 클릭

 
time.sleep(2) # 2초 대기
driver.quit() # 브라우저 종료
