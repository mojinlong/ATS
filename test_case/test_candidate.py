#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/10/28 14:37 
# @Author   : 蓦然
# @File     : test_candidate.py
# Project   : ATS_AOTO
import pytest
import allure

from test_case.api.candidate import *
from test_case.enumeration_ats.candidate_enumerate import candidate_status
from faker import Faker

fake = Faker(locale='zh_CN')


@allure.feature("候选人流程冒烟")
class Test_Candidate:

    @pytest.mark.test
    @allure.title('候选人流程冒烟')
    def test_candidate_process(self):
        # # '''创建候选人:待筛选-筛选通过'''
        enumerates = candidate_status
        candidate = candidate_create(name=fake.name())
        if candidate[2] == enumerates.WAIT_FOR_SCREEN.value:
            update_candidate_status(name=candidate[0], uid=candidate[1], status=enumerates.SUCCESS_SCREEN.value)
        else:
            raise Exception('候选人{}状态错误'.format(candidate[0]))
        ''' 安排面试'''
        interview_create(uid=candidate[1])
        update_candidate_status(name=candidate[0], uid=candidate[1], status=enumerates.SUCCESS_SCHEDULED.value)
