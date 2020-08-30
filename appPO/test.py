#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml

from appPO.app import App


def get_contact():
    with open("./user.yaml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    return datas


class TestWexin:
    def setup(self):
        """
        启动app
        """
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()
    @pytest.mark.parametrize('name', get_contact())
    def test_addcontact(self, name):
        mypage = self.main.gotolist().gotouserlist().gotodeluser(name).gotodel().gotosearchuser().gotosearch()

        assert mypage == '无搜索结果'