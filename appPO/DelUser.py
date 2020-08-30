#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appPO.basePage import basepage


class deluser(basepage):
    def gotodel(self):
        from appPO.DelList import dellist
        # 点击删除
        #self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/e_1").click()
        # 点击确定
        #self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/bfe").click()
        from appium.webdriver.common.mobileby import MobileBy
        self.find(MobileBy.ID, "com.tencent.wework:id/e_1").click()
        self.find(MobileBy.ID, "com.tencent.wework:id/bfe").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hjz").click()
        return dellist(self.driver)