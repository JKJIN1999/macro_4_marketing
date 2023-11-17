#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 온기디자인 홈페티지 올리는 매크로 입니다.
# 문의사항은 JKJIN1999 github repository 또는 jugyeongkim911@gmail.com 으로 문의 부탁드립니다.


# In[27]:


import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
from datetime import datetime


# In[28]:


#로그 생성
logging.basicConfig(
    filename="./log.txt",
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO,
    datefmt='%m/%d/%Y %I:%M:%S %p',
)


# In[29]:


logging.info("Started ongi_macro")
driver = webdriver.Chrome()
driver2 = webdriver.Chrome()
clickCount = 0
driver2.get("https://ongidesignhaus.com/cband-me")
time.sleep(1)
driver.get('https://search.naver.com/search.naver?nso=&page=2&query=%EC%98%A8%EA%B8%B0%EB%94%94%EC%9E%90%EC%9D%B8&sm=tab_pge&start=1&where=web')
time.sleep(3)
pageCollected = driver.find_elements(By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/section/div/ul[@class="lst_total"]/li')


# In[30]:


## 텍스트 정리후 비교 수식
def volume_check():
    try:
        inVolume = True
        check_text = driver2.find_element(By.XPATH, "/html/body/table[2]/tbody/tr[2]/td[3]").text.split("/")
        print(check_text)
        if (check_text[2][-2:]) == "GB":
            if (float(check_text[2][:-2]) >= 7.0):
                logging.error("Error on volume_check function : Server Storage is Out!")
                inVolume = False
    except:
        logging.error("Error on volume_check function : Try Error!")
        inVolume = False
    return inVolume


# In[31]:


def webpage_clicker(clickCount):
    isFound = False
    isError = False
    for li in pageCollected:
        li_element = li.find_element(By.CLASS_NAME, "total_wrap").find_element(By.CLASS_NAME, "total_group").find_element(By.CLASS_NAME, "total_tit").find_element(By.CLASS_NAME, "link_tit")
        link_text = li_element.get_attribute('href')
        if link_text == "https://ongidesignhaus.com/":   
            isFound = True
            while volume_check():
                try:
                    li_element.click()
                    time.sleep(4)
                    driver.switch_to.window(driver.window_handles[-1])
                    driver.close()
                    time.sleep(4)
                    driver.switch_to.window(driver.window_handles[0])
                    clickCount += 1
                except:
                    logging.error("Error while running ongi_macro")
                    logging.info("{} clicks were done before error".format(clickCount))
                    isError = True
                    break
    if(isFound==False):    
        logging.error("Error on naver_page_open function: No page found!")
    else:
        if(isError):
            logging.error("There has been an error during while loop")


# In[ ]:


# ongidesignhaus.com/cband-me  의 사용량 실시관 확인후 7G 이상 넘으면 강제 다운

def main():
    webpage_clicker(clickCount)
    driver.quit()
    driver2.quit()
    logging.info("Macro has been finished. Total : {} amount of clicks were performed.".format(clickCount))
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




