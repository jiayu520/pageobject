# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


from pageobject3.page.add_member import AddMember
from pageobject3.page.base_page import BasePage


class Index(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"
    def goto_add_member(self):
        #self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_item_title').click()
        # self.find(By.CSS_SELECTOR,'.index_service_cnt_item_title').click()
        self.find(By.ID,"menu_contacts").click()
        def wait(driver):
            ele_len = len(self.finds(By.ID,"username"))#这里调用finds返回一个列表才有长度
            if ele_len < 1:
                self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member").click()
            return ele_len >= 1
        self.wait_for(wait)

        return AddMember(reuse=True)#实例化AddMember
    def imporrt_address(self):
        pass
    def member_join(self):
        pass