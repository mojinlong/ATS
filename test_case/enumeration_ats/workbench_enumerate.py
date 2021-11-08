#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/11/5 15:06 
# @Author   : 蓦然
# @File     : workbench_enumerate.py
# Project   : ATS
from enum import Enum, unique


@unique
class schedule_tab(Enum):
    """
        日程tab
            全部、- ALL
            面试、- INTERVIEW
            入职、- ENTRY
            提醒、- REMIND
    """
    TAB_ALL = "ALL"

    TAB_INTERVIEW = "INTERVIEW"

    TAB_ENTRY = "ENTRY"

    TAB_REMIND = "REMIND"
