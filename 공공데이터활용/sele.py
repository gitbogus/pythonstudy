from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome = webdriver.Chrome('chromedriver.exe')
chrome.get('https://google.com')

input_box= chrome.find_element_by_css_selector('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
input_box.send_keys('아시아나항공주가')
input_box.send_keys(Keys.ENTER)

print(Keys.ENTER)
# input_box.submit()
# print(input_box)
link = chrome.find_element_by_css_selector('#rso > div:nth-child(1) > div > div > div > div > div > div.yuRUbf > a')
link.click()
link = chrome.find_element_by_css_selector('#coronaState_temp > div.mo-mlk > a')
link.click()
# link = chrome.find_element_by_css_selector('#midSearchQuery')
# link.click()
# link = chrome.find_element_by_css_selector('#coronaState_temp > div.mo-mlk > a')
# link.click()

id_input = chrome.find_element_by_css_selector('#midSearchQuery')
#id_input.click()
# id_pass_input = chrome.find_element_by_css_selector('#pw')
# submit = chrome.find_element_by_css_selector('#midSearchForm > div.mainSearch > div > button')
id_input.send_keys('아시아나항공주가')
id_input.send_keys(Keys.ENTER)
print(Keys.ENTER)
# id_pass_input.send_keys('qhrdjd159!@')
# submit.click()

# chrome.switch_to.alert
# alert.accept() # 정보창확인
# print(alert.text)

chrome.time.sleep(3) # 3초간 정지
chrome.quit()