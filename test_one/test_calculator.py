# -*- coding: utf-8 -*-
import allure
import pytest
import yaml

from test_one.Calculator import Cal


@pytest.fixture()
def funt():
    print("开始")
    yield
    print("结束")


def get_adddata():
    with open('./cal.yml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        ids = mydatas['add']['ids']
    return [adddatas, ids]

@allure.feature("加法测试")
class Test_add:

    def setup_class(self):
        print("加法测试开始")
        self.cal = Cal()

    def teardown_class(self):
        print("加法测试结束")

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,result', get_adddata()[0], ids=get_adddata()[1])
    @allure.story(f"{get_adddata()[1]}")
    def test_add(self, a, b, result,funt):
        assert result == round(self.cal.add(a, b), 2)

def get_divdata():
    with open('./cal.yml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        divdatas = mydatas['div']['datas']
        ids = mydatas['div']['ids']
    return [divdatas, ids]

@allure.feature("除法测试")
class Test_div:

    def setup_class(self):
        print("除法测试开始")
        self.cal = Cal()

    def teardown_class(self):
        print("除法测试结束")

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,result', get_divdata()[0], ids=get_divdata()[1])
    @allure.story(f"{get_adddata()[1]}")
    def test_div(self, a, b, result,funt):
        assert result == round(self.cal.div(a, b), 2)

def get_subdata():
    with open('./cal.yml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        subdatas = mydatas['sub']['datas']
        ids = mydatas['sub']['ids']
    return [subdatas, ids]

@allure.feature("减法测试")
class Test_sub:

    def setup_class(self):
        print("减法测试开始")
        self.cal = Cal()

    def teardown_class(self):
        print("减法测试结束")

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,result', get_subdata()[0], ids=get_subdata()[1])
    @allure.story(f"{get_adddata()[1]}")
    def test_sub(self, a, b, result,funt):
        assert result == round(self.cal.sub(a, b), 2)


def get_muldata():
    with open('./cal.yml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        muldatas = mydatas['mul']['datas']
        ids = mydatas['mul']['ids']
    return [muldatas, ids]

@allure.feature("乘法测试")
class Test_mul:

    def setup_class(self):
        print("乘法测试开始")
        self.cal = Cal()

    def teardown_class(self):
        print("乘法测试结束")


    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,result', get_muldata()[0], ids=get_muldata()[1])
    @allure.story(f"{get_adddata()[1]}")
    def test_mul(self, a, b, result,funt):
        assert result == round(self.cal.mul(a, b), 2)



