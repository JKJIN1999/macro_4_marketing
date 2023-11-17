#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 온기디자인 홈페티지 올리는 매크로 입니다.
# 문의사항은 JKJIN1999 github repository 또는 jugyeongkim911@gmail.com 으로 문의 부탁드립니다.


# In[2]:


import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
from datetime import datetime


# In[3]:


#로그 생성
logging.basicConfig(
    filename="./log.txt",
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO,
    datefmt='%m/%d/%Y %I:%M:%S %p',
)


# In[4]:


def naver_page_open():
    try:
        time.sleep(4)
        pageCollected = driver.find_elements(By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/section/div/ul[@class="lst_total"]/li')
        for li in pageCollected:
            a = li.find_element(By.CLASS_NAME, "total_wrap").find_element(By.CLASS_NAME, "total_group").find_element(By.CLASS_NAME, "total_tit").find_element(By.CLASS_NAME, "link_tit")
            link_text = a.get_attribute('href')
            if link_text == "https://ongidesignhaus.com/":
                a.click()
                time.sleep(2)
                break
    except:
        logging.error("Error on naver_page_open function")


# In[5]:


def google_page_open():
    try:
        time.sleep(5)
        pageCollected = driver.find_elements(By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/section/div/ul[@class="lst_total"]/li')
        for li in pageCollected:
            a = li.find_element(By.CLASS_NAME, "total_wrap").find_element(By.CLASS_NAME, "total_group").find_element(By.CLASS_NAME, "total_tit").find_element(By.CLASS_NAME, "link_tit")
            link_text = a.get_attribute('href')
            if link_text == "https://ongidesignhaus.com/":
                a.click()
                time.sleep(2)
                break
    except:
        logging.error("Error on google_page_open function")


# In[6]:


def auto_clicker():
    naver_page_open()
    #google_page_open()
    time.sleep(2)
    driver.quit()
    time.sleep(1)


# In[7]:


## 텍스트 정리후 비교 수식
def volume_check(driver2):
    try:
        inVolume = True
        check_text = driver2.find_element(By.XPATH, "/html/body/table[2]/tbody/tr[2]/td[3]").text.split("/")
        print(check_text)
        if (check_text[2][-2:]) == "GB":
            if (float(check_text[2][:-2]) >= 5.0):
                inVolume = False
    except:
        logging.error("Error on volume_check function")
        inVolume = False
    return inVolume


# In[ ]:


# ongidesignhaus.com/cband-me  의 사용량 실시관 확인후 5G 이상 넘으면 강제 다운
clickCount = 0
driver2 = webdriver.Chrome()
driver2.get("https://ongidesignhaus.com/cband-me")
while volume_check(driver2):
    try:
        driver = webdriver.Chrome()
        driver.get('https://search.naver.com/search.naver?nso=&page=2&query=%EC%98%A8%EA%B8%B0%EB%94%94%EC%9E%90%EC%9D%B8&sm=tab_pge&start=1&where=web')
        auto_clicker()
        clickCount += 1
    except:
        logging.error("Error while running ongi_macro")
        logging.info("{} clicks were done before error".format(clickCount))
driver2.quit()
logging.info("Macro has been finished. Total : {} amount of clicks were performed.".format(clickCount))


# In[ ]:





# In[ ]:




