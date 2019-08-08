#测试人员管理
from tests.testcases_address_list.case_api import *
import time
import sys
import allure

@allure.feature('测试成员功能')
class TestUser():
    uid = "FrankWang" + str(time.time())
    @allure.story('成员模块')
    @allure.testcase('对成员增删改查')
    def test_user(self):
        with allure.step("增加成员"):
            url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
            params = {"access_token": Utils.get_token()}
            uid = "FrankWang" + str(time.time())
            mobile = str(time.time()).replace(".", "")[0:11]
            test_user_data = str(Utils.parse(sys.path[0] + "/tests/testcases_address_list/user_create.json", {
                "name": uid,
                "title": "学员",
                "email": mobile + "@qq.com",
                "mobile": mobile
        }))
            test_user_data = test_user_data.encode('utf-8')
            ApiUser() \
                .set_url(url=url) \
                .set_params(params=params) \
                .set_data(data=test_user_data) \
                .run() \
                .validate("status_code", 200)

        with allure.step("查询成员"):
            url2 = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
            params2 = {"access_token": Utils.get_token(),'userid':uid}
            ApiUser() \
                .set_url(url=url2)\
                .set_params(params=params2)\
                .run() \
                .validate("status_code", 200)

        with allure.step("删除成员"):
            url3 = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
            params3 = {"access_token": Utils.get_token(),'userid':uid}
            ApiUser() \
                .set_url(url=url3)\
                .set_params(params=params3)\
                .run() \
                .validate("status_code", 200)
