import sys
sys.path.insert(0,)


import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# 스크래핑 함수
def scraping():
    wd = webdriver.Chrome('chromedriver', options=chrome_options)
    wd.implicitly_wait(3)

    news_idx = 0
    news_df = pd.DataFrame(colums=("Title", "Press", "DateTime","Article", "Nice", "Good", "Sad", "Angry", "Want", "Subs", "URL"))

    news_url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=008&aid=0004599612"
    wd.get(news_url)

    news_df.loc[news_idx] = news_scraping(news_url, wd)
    news_idx += 1

    wd.close()

    return 

news_df = scraping()

# 뉴스 스크래핑 함수
def news_scraping(news_url, wd)
    press = wd.find.element_by_xpath('//*[@id="main_content"]/div[1]/div[1]/a/img').get_attribute('title').text
    title = wd.find_element_by_id('articleTitle').txt
    datetime = wd.find_element_by_class_name('t11').txt
    article = wd.find_element_by_id('articleBodyContents').txt
    article = article.replace("// flash 오류를 우회하기 위한 함수 추가"," ")
    article = article.replace("function _flash_removeCallback() {}"," ")
    article = article.replace("\n","")
    article = article.replace("\t","")

    nice  = wd.find_element_by_xpath('//*[@id="spiLayer"]/div[1]/ul/li[1]/a')
    good  = wd.find_element_by_xpath('//*[@id="spiLayer"]/div[1]/ul/li[2]/a')
    sad  = wd.find_element_by_xpath('//*[@id="spiLayer"]/div[1]/ul/li[3]/a')
    angry  = wd.find_element_by_xpath('//*[@id="spiLayer"]/div[1]/ul/li[4]/a')
    want  = wd.find_element_by_xpath('//*[@id="spiLayer"]/div[1]/ul/li[5]/a')
    subs  = wd.find_element_by_xpath('//*[@id="toMainContainer"]/a')
    print("뉴스 : ", [title, press, datetime, article, nice, good, sad, angry, want, subs, news_url])

    return 


# 보류