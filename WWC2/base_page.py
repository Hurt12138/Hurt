#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        option = Options()
        option.debugger_address = "localhost:9222"
        db = shelve.open('mydb')
        self._driver = ""
        if driver is None:
            self._driver = webdriver.Chrome(options=option)
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

        #self._driver.get("https://work.weixin.qq.com/wework_admin/frame")
        c1 = self._driver.get_cookies()
        db['cookie'] = c1
        cookies = db['cookie']
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self._driver.add_cookie(cookie)
        if self._base_url != "":
            self._driver.get(self._base_url)
        #self._driver.get("https://work.weixin.qq.com/wework_admin/frame")

        self._driver.implicitly_wait(3)

    def find(self,by ,locator):
        return self._driver.find_element(by,locator)


