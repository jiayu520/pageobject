# -*- coding: utf-8 -*-
import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTest():
    def setup_method(self):
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.debugger_address = "127.0.0.1:9222"
        #self.driver = webdriver.Chrome(options=chrome_opts)#浏览器复用，在已登录的界面接着操作，注意需要在cmd中输入chrome -remote-debugging-port=9222端口要对应
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
    # def teardown_method(self):
    #     self.driver.quit()

    def test_test(self):
        time.sleep(3)
        #self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_item_title").click()#这步会在已经登录的企业微信界面操作

        # cookies = self.driver.get_cookies()
        # with open("cookies.txt",'w') as f:
        #     json.dump(cookies,f)#将cookie存入txt中
        with open("cookies.txt",'r') as f:
            cookies:list[dict]=json.load(f)#将TXT中的内容加载到f,前面的作用是告诉变量的数据类型，cookie是一个列表里面包的字典，后续调用是输入点就会有list的方法
            for cookie in cookies:
                self.driver.add_cookie(cookie)
                #print(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_item_title").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,"#username").send_keys("hello")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,"#memberAdd_acctid").send_keys("12334")
