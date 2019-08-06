import time
import pystache
import requests
import yaml
import logging

#pystache支持变量替换、列表遍历、条件判断等

class Utils:
    @classmethod
    def parse(self, template_path, dict):
        template = "".join(open(template_path).readlines())
        #支持把temp中的{{值}} 替换成dict中给的值
        return pystache.render(template, dict)

    @classmethod
    def udid(self):
        return str(time.time()).replace(".", "")[0:11]


    logging.basicConfig(level=logging.DEBUG)
    _token= ""
    @classmethod
    def get_token(cls):
        if len(cls._token)==0:
            cls._token=cls.get_token_new()
        return cls._token

    @classmethod
    def get_token_new(cls):
        conf=yaml.safe_load(open("weixin.yaml"))
        logging.debug(conf["env"])

        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                     params={"corpid": conf["env"]["corpid"],
                             "corpsecret": conf["env"]["secret"]}
                     ).json()
        return r["access_token"]
