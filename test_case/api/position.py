#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/10/21 10:59 
# @Author   : 蓦然
# @File     : position.py
# Project   : ATS

from faker import Faker
from test_case.common import request
from test_config import param_config

faker = Faker(locale="zh_CN")
categoryTreeName = param_config.categoryTreeName


def contactSubjectCuSelect(sid):
    """
        查询签约主体
    """
    url = '/pic/api/position/contactSubjectCuSelect'
    body = {
        "pageNum": 1,
        "pageSize": 1000000,
        "queryWord": ""
    }
    response = request.post_body(url, body=body)
    # print(response)
    for subject in response['data']['records']:
        if sid in subject['id']:
            print("签约主体: {}创建成功".format(sid))
            break
        else:
            raise Exception("签约主体查询失败, 检查是否创建成功")
    return sid


def create_subject(name):
    """
        签约主体
    """
    url = '/pic/api/position/create_subject'
    body = {
        "name": name
    }
    response = request.post_body(url, body=body)
    return response['data']['id']


def categoryTree(name=categoryTreeName):
    """
        职位类别
    """
    url = '/pic/api/position/categoryTree'
    response = request.post(url)
    cid = ''
    for x in response['data']:
        for y in x['children']:
            for z in y['children']:
                if name == z['name']:
                    cid = z['id']
    return cid


def position_create(publicFlag=True, notifyFlag=True, categoryId=categoryTree):
    """
    请求参数
        参数名称    参数说明    请求类型    是否必须    数据类型
        addressHouseNumber	门牌号		false   string
        categoryId      职位所属的类别id		false   integer(int64)
        deptEmployeeCount	部门现有人数		false   integer(int32)
        deptVacancyCount	部门缺编人数		false   integer(int32)
        description	    职位描述		false       string
        educationLimit	学历要求 学历 0-其他、1-小学、2-初中、3-高中、4-中专、5-大专、6-本科、7-硕士研究生、8-博士研究生、9-博士后、10-mba
        employManagers	用人经理		false   array
        name	        职位名称		false   string
        notifyFlag	    是否通知 0-不通知 1-通知		false   boolean
        planRecruitNum	计划招聘人数	false   integer(int32)
        publicFlag	    是否公开 0-不公开 1-公开		false   boolean
        regional	    区域		    false   string
        resumeManagers	简历负责人	false   array   string
        salaryLower	    薪资下限(单位:千)		false   integer(int32)
        salaryMonth     薪资月数		false   integer(int32)
        salaryUnit	    薪资单位(不是全职的时候) 1:元/时 2:元/日 3:元/月 4:元/年		false   integer(int32)
        salaryUppper	薪资上限(单位:千)		false   integer(int32)
        subjectId	主体id		false   integer(int64)
        tagDTOList	标签集合		false   array
        tagId	标签id		false   integer
        tagName	标签名称		false   string
        thirdDeptId	职位关联的第三方部门id(招聘部门)，如企微的部门id		false   string
        type	职位类型 1-全职 2-兼职 3-实习 4-校招 5-其他		false   integer(int32)
        workAddress	工作详细地点		false   string
        workAddressLat	工作地址纬度		false   number
        workAddressLng	工作地址经度		false   number
        workAddressShort	工作简短地点		false   string
        workYears	工作年限 0:1年以下 1:1-3年 2:3-5年 3:5-10年 4:10年以上 5：经验不限		false   integer(int32)
    """
    body = {
        "id": None,
        "name": "测试开发",
        "publicFlag": publicFlag,
        "notifyFlag": notifyFlag,
        "categoryId": categoryId,
        "subjectId": "56752118371061760",
        "type": 1,
        "regional": "上海市",
        "description": "职位描述",
        "workYears": 0,
        "educationLimit": 6,
        "planRecruitNum": "100",
        "deptVacancyCount": "100",
        "deptEmployeeCount": "0",
        "thirdDeptId": "62",
        "resumeManagers": ["MoJinLong"],
        "employManagers": ["MoJinLong"],
        "salaryLower": "10000",
        "salaryUppper": "30000",
        "salaryMonth": 12,
        "salaryUnit": 3,
        "workAddress": "上海市徐汇区斜土路2899号(近星游城)",
        "workAddressLat": 31.185694,
        "workAddressLng": 121.441156,
        "workAddressShort": "光启文化广场",
        "addressHouseNumber": "A栋2楼202"
    }
    request.post_body()
    pass


def position_delete():
    """
    接口描述 : 删除职位
    request : post
    参数名称    参数说明    类型
    id         id        integer
    """
    url = '/pic/api/position/delete'
    pass


def position_create_subject():
    pass


def position():
    pass


def position():
    pass


def position():
    pass


def position():
    pass


def position():
    pass


def position():
    pass


def position():
    pass


def position():
    pass


if __name__ == '__main__':
    subjectId = create_subject(name="{}公司测试{}签约主体".format(faker.company_prefix(), faker.name()))
    contactSubjectCuSelect(subjectId)
