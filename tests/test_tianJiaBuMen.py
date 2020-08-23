# -*- coding: utf-8 -*-
import shelve

from selenium.webdriver.common.by import By
from WWC2.main import Main




class TestTJBM():
    def setup(self):
        self.main = Main()
    def test_tjbm(self):
        self.main.gototjbm().tjbm()
        assert "新建部门成功" == self.main.find(By.ID, "js_tips").text


