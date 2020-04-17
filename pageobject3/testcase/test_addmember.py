# -*- coding: utf-8 -*-
from time import sleep

from page.base_page import BasePage
from pageobject3.page.index import Index


class TestAddMember():
    def setup(self):
        self.index = Index(reuse=True)
    def test_addmember(self):
        add_number = self.index.goto_add_member()#goto_add_member实例化了addMember
        add_number.add_member()
        sleep(3)
        assert "123" in add_number.get_second()