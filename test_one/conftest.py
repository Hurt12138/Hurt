# -*- coding: utf-8 -*-
from typing import List

import pytest


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')




@pytest.fixture(scope='module', autouse=True)
def firstone():
    print("计算开始")
    yield
    print("计算结束")