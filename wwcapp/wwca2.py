#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDelUser:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["noReset"] = "true"
        caps["dontStopAppOnReset"] = "true"
        caps["skipDeviceInitialization"] = "true"
        caps["unicodeKeyBoard"] = "true"
        caps["resetKeyBoard"] = "true"


        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_delete_user(self):
        #点击通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        #点击右上角设置图标
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk4").click()
        #点击刘鹏
        self.driver.find_element(MobileBy.XPATH, "//*[@text='刘鹏']").click()
        #self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b53").click()
        #点击删除
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/e_1").click()
        #点击确定
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/bfe").click()
        #点击右上XX
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hjz").click()
        #点击右上角搜索
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk9").click()
        #输入
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/g75").send_keys("刘鹏")
        assert "无搜索结果" == self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/c5m").text





