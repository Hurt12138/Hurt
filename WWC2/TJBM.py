#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from WWC2.base_page import BasePage


class Tjbm(BasePage):
    def tjbm(self):
        #BasePage.find(self, By.NAME, "name").click()
        BasePage.find(self,By.NAME,"name").send_keys("HR")
        BasePage.find(self,By.LINK_TEXT, "选择所属部门").click()
        BasePage.find(self,By.CSS_SELECTOR, ".jstree-2 #\\31 688852002540478_anchor").click()
        BasePage.find(self,By.LINK_TEXT, "确定").click()
        return True


