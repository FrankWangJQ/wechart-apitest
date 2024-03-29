
import requests
#设计父类 各个用例类继承父类
class BaseApi(object):
#设置通用变量
    method = "GET"
    url = ""
    params = {}
    headers = {}
    cookies = {}
    data = {}
    json = {}

    def __init__(self):
        self.response = None
#初始化各请求参数
    def set_params(self, **params):
        self.params = params
        return self

    def set_cookie(self, key, value):
        self.cookies.update({key: value})
        return self

    def set_data(self, data):
        self.data = data
        return self

    def set_json(self, json_data):
        self.json = json_data
        return self
#封装发送请求
    def run(self, session=None):
        session = session or requests.sessions.Session()
        self.response = session.request(
            self.method,
            self.url,
            params=self.params,
            cookies=self.cookies,
            headers=self.headers,
            data=self.data,
            json=self.json
        )
        return self
#封装函数，传入key值  返回对应的value   key可以对应response值 header中的值  以及json中的值
    def extract(self, field):
        value = self.response
        for _key in field.split("."):
            if isinstance(value, requests.Response):
                if _key == "json()":
                    value = self.response.json()
                else:
                    value = getattr(value, _key)
            elif isinstance(value, (requests.structures.CaseInsensitiveDict, dict)):
                value = value[_key]
        return value
#封装断言，可以断言response.key response.heder.key response.json.key
    def validate(self, key, expected_value):
        actual_value = self.extract(key)
        assert actual_value == expected_value
        return self

    def get_response(self):
        return self.response
