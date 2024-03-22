# -*- coding: utf-8 -*-
# filename: menu.py

import requests
import json

class Menu(object):
    def get_menu_url(self):
        grant_type = "client_credential"
        appid = "wxbf0a634260bac842"
        secret = "a749fddccf732f02c80fcb05a0763085"
        token_url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}".format(appid, secret)
        response = requests.get(token_url)
        result = json.loads(response.text)
        if "access_token" not in result:
            raise ValueError(result["errmsg"])
        return "https://api.weixin.qq.com/cgi-bin/menu/create?access_token={}".format(result["access_token"])

    def create(self):
        menu_url = self.get_menu_url()
        menu_data = {
            "button":[
            {   
              "type":"click",
              "name":"今日歌曲",
              "key":"V1001_TODAY_MUSIC"
            },
            {
               "name":"菜单",
               "sub_button":[
               {    
                   "type":"view",
                   "name":"搜索",
                   "url":"http://www.soso.com/"
                },
                {
                    "type":"miniprogram",
                    "name":"wxa",
                    "url":"http://mp.weixin.qq.com",
                    "appid":"wx286b93c14bbf93aa",
                    "pagepath":"pages/lunar/index"
                },
                {
                   "type":"click",
                   "name":"赞一下我们",
                   "key":"V1001_GOOD"
                }]
            }]
        }
        response = requests.post(menu_url, data=json.dumps(menu_data).encode("utf-8"))
        result = json.loads(response.text)
        if result["errcode"] == 0:
            print "菜单创建成功"
        else:
            print "菜单创建失败：{}".format(result["errmsg"])
