#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver

from appPO.MainPage import mainpage
from appPO.basePage import basepage


class App(basepage):

    def start(self):

        if self.driver == None:
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

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub" , caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self) -> mainpage:
        return mainpage(self.driver)