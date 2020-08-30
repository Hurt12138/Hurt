#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appPO.basePage import basepage


class userlist(basepage):
    def gotodeluser(self,name):
        from appPO.DelUser import deluser
        #self.driver.find_element(MobileBy.XPATH, "//*[@text='刘鹏']").click()
        from appium.webdriver.common.mobileby import MobileBy
        self.find(MobileBy.XPATH, f"//*[@text='刘鹏']").click()
        return deluser(self.driver)