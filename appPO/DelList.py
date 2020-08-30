#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appPO.UserList import userlist
from appPO.basePage import basepage
from appPO.searchuser import searchuser


class dellist(basepage):
    def gotouserlist(self):
        from appium.webdriver.common.mobileby import MobileBy
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk4").click()
        self.find(MobileBy.ID, "com.tencent.wework:id/hk4").click()
        return userlist(self.driver)
    def gotosearchuser(self):
        from appium.webdriver.common.mobileby import MobileBy

        #self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk9").click()
        self.find(MobileBy.ID, "com.tencent.wework:id/hk9").click()
        return searchuser(self.driver)