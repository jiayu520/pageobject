# -*- coding: utf-8 -*-
from time import sleep

from page.base_page import BasePage
from pageobject2.page.index import Index


class TestAddMember():l
    def setup(self):
        self.index =Index()
    def test_addmember(self):
        add_number = self.index.goto_add_member()#goto_add_member实例化了addMember
        add_number.add_member()
        sleep(3)
        assert add_number.get_second() == '1234'