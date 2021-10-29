#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/10/13 11:22 
# @Author   : 蓦然
# @File     : candidate.py
# Project   : ATS_AUTO
from enum import Enum, unique

@unique
class candidate_status(Enum):
    """
    status: 状态
            0-初筛淘汰或面试淘汰
            10-待筛选
            20-筛选通过
            30-已安排面试
            40-已面试
            50-拟录用
            60-待入职
            70-已入职
    """
    ELIMINATE = 0  # 淘汰的VALUE被设定为0

    WAIT_FOR_SCREEN = 10    # 待筛选

    SUCCESS_SCREEN = 20    # 筛选通过

    INTERVIEW_SCHEDULED = 30    # 已安排面试

    SUCCESS_SCHEDULED = 40    # 已面试

    PROPOSED_EMPLOYMENT = 50    # 拟录用

    TO_BE_EMPLOYED = 60    # 待入职

    EMPLOYED = 70   # 已入职
