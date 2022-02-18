from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights"
browser.get(url) # url로 이동

# 가는 날 선택 클릭
elem = browser.find_element_by_class_name("tabContent_option__2y4c6")
elem.click()

# 이번달 27일, 28일 선택
browser.find_elements_by_link_text("27")[0].click() #[0] -> 이번달
browser.find_elements_by_link_text("28")[0].click() #[0] -> 이번달