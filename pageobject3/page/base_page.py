# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

#他是用来封装有关driver的操作
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver=""#一个下划线表示私有变量
    base_url = ""
    def __init__(self,reuse = False):
        if reuse == True:
            opts = webdriver.ChromeOptions()
            opts.debugger_address="127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=opts)
        else:
            self._driver = webdriver.Chrome()
        if self.base_url != "":
            self._driver.get(self.base_url)
        self._driver.implicitly_wait(3)  # 隐式等待可以解决元素没有出现的问题（可能是网络或者什么原因导致元素没有加载出来）
    def find(self,by,locator):
        return self._driver.find_element(by,locator)
    def finds(self,by,locator):
        return self._driver.find_elements(by,locator)
    #显示等待
    def wait_for(self,fun):
        #如果fun返回了一个true，那么就退出显示等待
        WebDriverWait(self._driver,10).until(fun)