# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome('chromedriver')
# driver.get("http://www.google.com")

# search = driver.find_element_by_id('q')
# time.sleep(1)
# search.send_keys('파이썬')
# time.sleep(1)
# # search.send_keys(Keys.RETURN)
# search.submit()
# time.sleep(1)
# res = driver.find_element_by_css_selector('#rso > div:nth-child(1) > div:nth-child(2) > div > div.yuRUbf > a')
# res.click()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome('chromedriver')
# driver.get('https://www.google.com')
# search = driver.find_element_by_name('q')
# time.sleep(1)
# search.send_keys('파이썬')
# time.sleep(1)
# #search.send_keys(Keys.RETURN)
# search.submit()
# time.sleep(1)
# res=driver.find_element_by_css_selector('#rso > div:nth-child(1) > div:nth-child(2) > div.tF2Cxc > div > div.yuRUbf > a > h3 > span')
# res.click()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver')
driver.get('https://www.google.com')
search = driver.find_element_by_name('q')
time.sleep(1)
search.send_keys('파이썬')
time.sleep(1)
#search.send_keys(Keys.RETURN)
search.submit()
time.sleep(1)
#res=driver.find_element_by_css_selector('#rso > div:nth-child(1) > div:nth-child(2) > div > div.yuRUbf > a')
s='#rso > div:nth-child(1) > div:nth-child(2) > div.tF2Cxc > div.yuRUbf > a > h3 > span'
res=driver.find_element_by_css_selector(s)
res.click()
