#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/10/28 14:37 
# @Author   : 蓦然
# @File     : test_candidate.py
# Project   : ATS_AOTO
import pytest
import allure
from test_case.common_ats.candidate import *
from test_case.common_ats.enumeration_ats.candidate_enumerate import candidate_status
from faker import Faker
fake = Faker(locale='zh_CN')


@allure.feature("候选人流程冒烟")
class Test_Candidate:

    @pytest.mark.test
    @allure.title('候选人流程冒烟')
    def test_candidate_process(self):
        # # '''创建候选人:待筛选-筛选通过'''
        enumerates = candidate_status
        create = candidate_create(name=fake.name())
        if create[2] == enumerates.WAIT_FOR_SCREEN.value:
            update_candidate_status(name=create[0], uid=create[1], status=enumerates.SUCCESS_SCREEN.value)
        else:
            raise Exception('候选人{}状态错误'.format(create[0]))
        ''' 安排面试'''
        interview_create(uid=create[1])
        update_candidate_status(name=create[0], uid=create[1], status=enumerates.SUCCESS_SCHEDULED.value)
        back_tone_order_open_flag()
        # 背调套餐查询
        package = back_tone_order_choose_package("套餐A")
        # 发起背调
        id = candidate_page(name=create[0], phone=None)[0]
        candidate_detail(candidateId=id)
        back_tone_order_create(amount=package['amount'], candidateId=id, candidateIdCard=None, candidateName=create[0],
                               candidatePhoneNo=param_config.phone, clientContact=param_config.clientContact,
                               clientEmail=param_config.email, clientPhoneNo=param_config.phone, department=None,
                               email=param_config.email, itemList=package['itemList'], position="测试",
                               flag=package['flag'], productId=package['productId'], productName=package['productName'])
        back_tone_order_list(id)
