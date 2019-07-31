import requests
import sys
sys.path.append('D:\\Program Files (x86)\\python\\lib\\site-packages')
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from numpy import random as nr
import numpy as np
from pandas import Series,DataFrame
import pandas as pd
def get_one(url):
    browser=webdriver.Firefox()
    browser.get("https://www.toutiao.com/search/?keyword=NBA")
    time.sleep(2)
    pic_small=browser.find_element_by_class_name('drag-button')
    x,y=pic_small.location.values()
    time.sleep(2)
    p=1
    while p:
        ActionChains(browser).click_and_hold(pic_small).perform()
        time.sleep(0.5)
        dis=get_dis(browser)
        while dis>0:
            if dis>50:
                span=nr.randint(25, 35)
            else:
                span=nr.randint(15, 25)
            ActionChains(browser).move_by_offset(span, 0).perform()
            dis -= span
            time.sleep(nr.randint(10, 50) / 100)
        ActionChains(browser).release().perform()
        time.sleep(0.5)
        try:
            browser.find_element_by_css_selector('.verify-container')
            p = True
        except Exception:
            p = False
        time.sleep(0.5)
    response=browser.page_source
    return response

def get_dis(browser):
    time.sleep(0.5)
    pic_small = browser.find_element_by_id('validate-big')
    time.sleep(0.5)
    z=pic_small.get_attribute('src')
    response=requests.get(z)
    f=open(r'C:\Users\Liter Frye\Desktop\image2.jpg','wb')
    f.write(response.content)
    f.close()
    im = np.array(Image.open(r'C:\Users\Liter Frye\Desktop\image2.jpg').convert('L'))
    im[im < 140] = 0
    f = []
    for i in range(np.shape(im)[1] - 50):
        area = np.sum(im[50:110, i:i + 50])
        if i > 0:
            if area < f[1]:
                f = [i, area]
        else:
            f = [i, area]
    dis = f[0] - 10
    return dis

def main():
    response=get_one("https://www.toutiao.com/search/?keyword=NBA")
    print(response)

if __name__ == '__main__':
    main()

