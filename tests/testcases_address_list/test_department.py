import datetime
import json
import os

import pytest
import requests

import logging

from tests.utils import Utils

@allure.feature('测试部门功能')
class TestDepartment:
    @allure.testcase('测试用例：测试新增部门深度（字部门）')
    def test_create_depth(self, token):
        parentid = 1

        for i in range(2):
            data = {
                "name": "第九期_FrankWang_" + str(parentid)+ str(datetime.datetime.now().timestamp()),
                "parentid": parentid,
            }

            r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                              params={"access_token": token},
                              json=data,
                              # proxies={"https": "http://127.0.0.1:8080",
                              #          "http": "http://127.0.0.1:8080"},
                              # verify=False
                              ).json()
            logging.debug(r)
            parentid = r["id"]
            assert r["errcode"]==0

    @allure.testcase('测试用例：测试新增部门')
    def test_create_name(self, token):
        data = {
            "name": "第九期_FrankWang",
            "parentid": 1,
        }

        logging.debug(data)
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": token},
                          json=data
                          ).json()
        logging.debug(r)

    @allure.testcase('测试用例：使用不同语言新增部门')
    @pytest.mark.parametrize("name", [
        "广州研发中心",
        "東京アニメーション研究所",
        "도쿄 애니메이션 연구소",
        "معهد طوكيو للرسوم المتحركة",
        "東京動漫研究所"
    ])
    def test_create_order(self, name, token):
        data = {
            "name": name+Utils.udid(),
            "parentid": 1,
            "order": 1,
        }

        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": token},
                          json=data
                          ).json()

        #解密
        logging.debug(r)
        assert r["errcode"]==0

    @allure.testcase('测试用例：获取部门列表')
    def test_get(self, token):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                         params={"access_token": token }
                         ).json()

        logging.info(json.dumps(r, indent=2))

    @allure.testcase('测试用例：更新部门列表')
    def test_updata(self):
        pass

    @allure.testcase('测试用例：删除部门')
    def test_delete(self):
        pass
