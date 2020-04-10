# -*- coding: utf-8 -*-
from page.base_page import BasePage
from pageobject2.page.index import Index


class TestAddMember():
    def setup(self):
        self.index =Index()
    def test_addmember(self):
        self.index.goto_add_member().add_member()