# __author:"MOYA"
# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

import requests, json
import test_case.common.get_token as get_token, os
import test_case.common.logger as logger
from test_config import param_config, yamlconfig
headers = get_token.headers
api_url = param_config.api_url
upload_file_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'test_data/upload_file')
log = logger.Log()


def get_params(path, params, headers=headers):
    r = requests.get(api_url + path, headers=headers, params=params, verify=False)
    response = r.json()
    assert (r.status_code == 200)
    if response['code'] == 2:
        log.error('----------系统错误---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(params, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 1:
        log.warning('----------接口报错---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(params, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 0:
        log.info(
            '----------请求成功---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (path, json.dumps(params, ensure_ascii=False),
                                                                           json.dumps(response, ensure_ascii=False)))
    return response


def get_body(path, body, headers=headers):
    r = requests.get(api_url + path, headers=headers, json=body, verify=False)
    response = r.json()
    assert (r.status_code == 200)
    if response['code'] == 2:
        log.error('----------系统错误---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(body, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 1:
        log.warning('----------接口报错---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(body, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 0:
        log.info(
            '----------请求成功---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (path, json.dumps(body, ensure_ascii=False)
                                                                           , json.dumps(response, ensure_ascii=False)))
    return response


def get(path):
    r = requests.get(api_url + path, headers=headers, verify=False)
    response = r.json()
    assert (r.status_code == 200)
    if response['code'] == 2:
        log.error(
            '----------系统错误---------- \n 请求地址：%s \n 响应内容：%s' % (path, json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 1:
        log.warning(
            '----------接口报错---------- \n 请求地址：%s \n 响应内容：%s' % (path, json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 10000:
        log.info('----------请求成功---------- \n 请求地址：%s \n 响应内容：%s ' % (path, json.dumps(response, ensure_ascii=False)))
    return response


def get_notResp(path):
    r = requests.get(api_url + path, headers=headers, verify=False)
    assert (r.status_code == 200)
    return r


def post_body(path, body):
    r = requests.post(api_url + path, headers=headers, json=body, verify=False)
    response = r.json()
    assert (r.status_code == 200)
    if response['code'] == 50000:
        log.error('----------系统错误---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(body, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 40003:
        log.warning('----------接口报错---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(body, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 10000:
        log.info('----------post请求成功---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(body, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    return response


def post_params(path, params):
    r = requests.post(api_url + path, headers=headers, params=params, verify=False)
    response = r.json()
    assert (r.status_code == 200)
    if response['code'] == 2:
        log.error('----------系统错误---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(params, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 1:
        log.warning('----------接口报错---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(params, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 0:
        log.info('----------请求成功---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(params, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    return response


def post_body_01(path, body):
    r = requests.post(api_url + path, headers=headers, json=body, verify=False)
    response = r.json()
    assert (r.status_code == 200)
    yamlconfig.body_data.setdefault(path, body)
    return response


def post_file(path, file_name):
    Content_Type = headers.pop('Content-Type')
    files = {'file': open(os.path.join(upload_file_dir, file_name),
                          'rb')}
    r = requests.post(api_url + path, headers=headers, files=files, verify=False)
    response = r.json()
    assert (r.status_code == 200)
    if response['code'] == 2:
        log.error('----------系统错误---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, files, json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 1:
        log.warning('----------接口报错---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, files, json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 0:
        log.info('----------请求成功---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, files, json.dumps(response, ensure_ascii=False)))
    headers['Content-Type'] = Content_Type
    return response


def post(path):
    r = requests.post(api_url + path, headers=headers, verify=False)
    response = r.json()
    assert (r.status_code == 200)
    if response['code'] == 2:
        log.error(
            '----------系统错误---------- \n 请求地址：%s \n 响应内容：%s' % (path, json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 1:
        log.warning(
            '----------接口报错---------- \n 请求地址：%s \n 响应内容：%s' % (path, json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 0:
        log.info(
            '----------请求成功---------- \n 请求地址：%s \n 响应内容：%s' % (path, json.dumps(response, ensure_ascii=False)))
    return response


def delete_body(path, body):
    r = requests.delete(api_url + path, headers=headers, data=json.dumps(body), verify=False)
    response = r.json()
    assert (r.status_code == 200)
    if response['code'] == 2:
        log.error('----------系统错误---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(body, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 1:
        log.warning('----------接口报错---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(body, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 0:
        log.info('----------请求成功---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(body, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))

    return response


def delete_params(path, params):
    r = requests.delete(api_url + path, headers=headers, params=params, verify=False)
    response = r.json()
    assert (r.status_code == 200)
    if response['code'] == 2:
        log.error('----------系统错误---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(params, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 1:
        log.warning('----------接口报错---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(params, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 0:
        log.info('----------请求成功---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(params, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    return response


def delete(path):
    r = requests.delete(api_url + path, headers=headers, verify=False)
    response = r.json()
    assert (r.status_code == 200)
    if response['code'] == 2:
        log.error(
            '----------系统错误---------- \n 请求地址：%s \n 响应内容：%s' % (path, json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 1:
        log.warning(
            '----------接口报错---------- \n 请求地址：%s \n 响应内容：%s' % (path, json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 0:
        log.info(
            '----------请求成功---------- \n 请求地址：%s \n 响应内容：%s' % (path, json.dumps(response, ensure_ascii=False)))
    return response


def put_body(path, body):
    r = requests.put(api_url + path, headers=headers, data=json.dumps(body), verify=False)
    response = r.json()
    assert (r.status_code == 200)
    if response['code'] == 2:
        log.error('----------系统错误---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(body, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 1:
        log.warning('----------接口报错---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(body, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 0:
        log.info('----------请求成功---------- \n 请求地址：%s \n 传入参数：%s \n 响应内容：%s' % (
            path, json.dumps(body, ensure_ascii=False), json.dumps(response, ensure_ascii=False)))
    return response


def put(path):
    r = requests.put(api_url + path, headers=headers, verify=False)
    response = r.json()
    assert (r.status_code == 200)
    if response['code'] == 2:
        log.error(
            '----------系统错误---------- \n 请求地址：%s \n 响应内容：%s' % (path, json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 1:
        log.warning(
            '----------接口报错---------- \n 请求地址：%s \n 响应内容：%s' % (path, json.dumps(response, ensure_ascii=False)))
    elif response['code'] == 0:
        log.info(
            '----------请求成功---------- \n 请求地址：%s \n 响应内容：%s' % (path, json.dumps(response, ensure_ascii=False)))
    return response
