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
        候选人状态
    """
    ELIMINATE = 0  # 淘汰的VALUE被设定为0

    WAIT_FOR_SCREEN = 10  # 待筛选

    SUCCESS_SCREEN = 20  # 筛选通过

    INTERVIEW_SCHEDULED = 30  # 已安排面试

    SUCCESS_SCHEDULED = 40  # 已面试

    PROPOSED_EMPLOYMENT = 50  # 拟录用

    TO_BE_EMPLOYED = 60  # 待入职

    EMPLOYED = 70  # 已入职


@unique
class educationLimit(Enum):
    """
       学历要求
    """
    OTHER = 0  # -其他

    PRIMARY_SCHOOL = 1  # -小学

    JUNIOR_HIGH_SCHOOL = 2  # -初中

    HIGH_SCHOOL = 3  # -高中

    SECONDARY_SPECIALIZED_SCHOOL = 4

    JUNIOR_COLLEGE = 5  # -大专

    UNDERGRADUATE = 6  # -本科

    MASTER_DEGREE = 7  # -硕士研究生

    DOCTORAL_CANDIDATE = 8  # 博士研究生

    post_doctoral = 9  # 博士后

    MBA = 10  # -工商管理硕士


@unique
class salaryUnit(Enum):
    """
        薪资单位(不是全职的时候)
    """
    DOLLAR_TIME = 1  # 元 / 时

    DOLLAR_DAY = 2  # 元 / 日

    DOLLAR_MONTH = 3  # 元 / 月

    DOLLAR_YEAR = 4  # 元 / 年


@unique
class position_Type(Enum):
    """
        职位类型
    """
    FULL_TIME = 1  # 1   全职

    PART_TIME = 2  # 2   兼职

    INTERNSHIP = 3  # 3   实习

    SCHOOL_RECRUITMENT = 4  # 4   校招

    OTHER = 5  # 5   其他


@unique
class workYears(Enum):
    """
        工作年限
    """
    ZERO_TO_ONE_YEARS = 0  # 0:1年以下
    ONE_TO_THREE = 1
    THREE_TO_FIVE = 2
    FIVE_TO_TEN = 3
    TEN_YEARS = 4
    UNLIMITED_WORKING_EXPERIENCE = 5