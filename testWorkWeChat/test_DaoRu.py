# -*- coding: utf-8 -*-
import shelve

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


class Test_Daoru:
    def setup_method(self):
        option = Options()
        option.debugger_address = "localhost:9222"
        db = shelve.open('mydb')
        self._driver = webdriver.Chrome(options=option)
        self._driver.get("https://work.weixin.qq.com/wework_admin/frame")
        c1 = self._driver.get_cookies()
        db['cookie'] = c1
        cookies = db['cookie']
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self._driver.add_cookie(cookie)
        self._driver.get("https://work.weixin.qq.com/wework_admin/frame")
        x = (By.ID,'check_corp_info')
        WebDriverWait(self._driver, 20).until(expected_conditions.presence_of_all_elements_located(x))
        self._driver.implicitly_wait(3)


    def teardown_methon(self):
        self.db.close()
        self._driver.quit()


    def test_denglu(self):
        #cookies = self._driver.get_cookies()
        # print(cookies)
        self._driver.find_element_by_css_selector("[node-type='import']").click()
        self._driver.find_element_by_id("js_upload_file_input").send_keys("D:\\pycharm\\Pwork\\Homework\\testWorkWeChat\\1.xlsx")
        self._driver.find_element_by_id("submit_csv").click()
        assert "前往查看" == self._driver.find_element_by_id("reloadContact").text
        self._driver.find_element_by_id("reloadContact").click()
