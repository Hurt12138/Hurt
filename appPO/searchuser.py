#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appPO.basePage import basepage


class searchuser(basepage):
    def gotosearch(self):
        from appium.webdriver.common.mobileby import MobileBy
        self.find(MobileBy.ID, "com.tencent.wework:id/g75").send_keys("刘鹏")
        return self.find(MobileBy.ID, "com.tencent.wework:id/c5m").text

