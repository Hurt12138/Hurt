#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from WWC2.TJBM import Tjbm
from WWC2.base_page import BasePage


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"
    def gototjbm(self):

        BasePage.find(self,By.ID,"menu_contacts").click()
        BasePage.find(self,By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        BasePage.find(self,By.LINK_TEXT, "添加部门").click()
        return  Tjbm(self._driver)
