from wechart_base_api_class.base_api import BaseApi
from tests.utils import Utils

#设计用例类
class ApiGet(BaseApi):

    url = "http://httpbin.org/get"
    params = {}
    method = "GET"
    headers = {"accept": "application/json"}


class ApiPost(BaseApi):

    url = "http://httpbin.org/post"
    method = "POST"
    params = {}
    headers = {"accept": "application/json"}
    #body = {'a':'b'}  #body 和 json不能同时参数化  body的优先级要高于json 这样就会只执行data
    json = {"abc": 123}


class ApiGetCookies(BaseApi):

    url = "http://httpbin.org/cookies"
    method = "GET"
    params = {}
    headers = {"accept": "application/json"}


class ApiGetSetCookies(BaseApi):

    url = "http://httpbin.org/cookies/set"
    method = "GET"
    params = {}
    headers = {"accept": "text/plain"}



#测试成员测试用例类
class ApiUser(BaseApi):
    method = "POST"
    params = {"access_token": Utils.get_token()}
    headers = {"accept": "application/json"}

    # def create(self, dict=None, data=None):
    #     return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
    #                          params={"access_token": Weixin.get_token()},
    #                          json=dict,
    #                          data=data
    #                          ).json()
    #
    # def list(self, department_id=1, fetch_child=0, **kwargs):
    #     return requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
    #                         params={"access_token": Weixin.get_token(),
    #                                 "department_id": department_id,
    #                                 "fetch_child": fetch_child
    #                                 }
    #                         ).json()
