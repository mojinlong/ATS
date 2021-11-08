# _*_ coding: utf-8 _*_
# @Time     : 2021/9/10 10:58 
# @Author   : 蓦然
# !/usr/bin/env python
# @File     : get_token.py
# Project   : ATS

import requests
import urllib3
import test_config.param_config as param_config
urllib3.disable_warnings()
# login_phone = param_config.login_phone
# login_pwd = param_config.login_pwd
api_url = "https://ats-test.51zhaopin.cn"
param_token = param_config.token
headers = {}


def login():
    global headers
    payload = {
        'code': 110120,
        'suiteId': 'wwbddcd1884a9dc2c5',
        'state': 'wwbddcd1884a9dc2c5'
    }
    r = requests.get(api_url + '/pic/api/login/wework/third/code', params=payload, verify=False)
    try:
        assert r.json()['code'] == 10000
        assert r.json()['data']['expire'] != ""
        assert r.headers['Authorization'] != ""
        # print(r.headers['Authorization'])
    except Exception:
        raise Exception(r.json())

    # token = r.headers['Authorization']
    token = param_token
    # headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    return headers


login()
