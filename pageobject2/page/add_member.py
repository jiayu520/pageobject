# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from pageobject2.page.base_page import BasePage


class AddMember(BasePage):
    def add_member(self):
        #在添加成员页面输入内容
        self.driver.find_element_by_id("username").send_keys("123")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("ssss")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("13254678965")
        self.driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()#点击保存

    def get_second(self):
        return self.driver.find_element(By.CSS_SELECTOR,"#member_list tr:nth-child(2) td:nth-child(2)").get_attribute("title")#定位到元素并且获取tittle属性