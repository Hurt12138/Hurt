#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from appPO.basePage import basepage


class mainpage (basepage):
    # 点击通讯录

    def gotolist(self):
        self.find(MobileBy.XPATH,"//*[@text='通讯录']").click()
        from appPO.DelList import dellist

        return dellist(self.driver)