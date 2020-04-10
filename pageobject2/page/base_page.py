# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self,driver:WebDriver=None):#参数中的driver要指定类型，python才能识别
        self.driver=None#让Python知道一个实例变量
        if driver is None:
            opts = webdriver.ChromeOptions()
            opts.debugger_address="127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opts)
            self.driver.implicitly_wait(3)#隐式等待可以解决元素没有出现的问题（可能是网络或者什么原因导致元素没有加载出来）
        else:
            self.driver = driver