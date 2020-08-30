#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class basepage:
    black_list=[]
    errorNum=0
    errorMax=10
    def __init__(self, driver:WebDriver=None):
        self.driver = driver

    def find(self, by, locator=None):
        try:
            emt =self.driver.find_element(*by) if isinstance(by, tuple) else self.driver.find_element(by, locator)
            self.errorNum=0
            return emt
        except Exception as e:
            self.errorNum+=1
            if self.errorNum>=self.errorMax:
                raise e
            for black in self.black_list:
                emts = self.driver.find_element(*black)
                if len(emts) > 0:
                    emts[0].click()
                    return self.find(by, locator)
            raise e
    def send(self,value,by,locator=None):
        try:
            f = self.find(by,locator).send_keys(value)
            self.errorNum = 0
            return f
        except Exception as e:
            self.errorNum+=1
            if self.errorNum>= self.erroMax:
                raise  e
            for black in self.black_list:
                emts = self.driver.find_element(*black)
                if len(emts) > 0:
                    emts[0].click()
                    return self.send(value, by, locator)
            raise e
    # def steps(self,path):
    #     with open(path , encoding="utf-8") as f:
    #         steps:list[dict]=yaml.safe_load(f)
    #         for step in steps:
    #             if "by" in step.keys():
    #             element = self.find(step["by"], step["locator"])
    #             if "action" in
    def find_by_scroll_and_click(self, text):


        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector()'
                   '.scrollable(true).instance(0))'
                   '.scrollIntoView(new UiSelector()'
                   f'.text("{text}").instance(0));')
        self.find(element).click()


    def get_toasttext(self):
        text = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text

        return text
