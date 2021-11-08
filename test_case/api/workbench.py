#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/11/5 13:39 
# @Author   : 蓦然
# @File     : workbench.py
# Project   : ATS
import datetime
import time
import datetime
from pprint import pprint

from test_case.common import request
from test_case.enumeration_ats.workbench_enumerate import *


# 工作台


def calendar_detail(tab):
    """
        我的日程
    """
    day_time = str(int(time.mktime(datetime.date.today().timetuple()))*1000)
    zeroPoint = int(time.time()) - int(time.time()-time.timezone) % 86400
    tomorrow = str((zeroPoint + 86400) * 1000)
    url = '/pic/api/workbench/v2/calendar_detail'
    body = {
        "startTime": day_time,
        "endTime": tomorrow,
        "tab": tab
    }
    response = request.post_body(url, body=body)
    pprint(response)
    return response


if __name__ == '__main__':
    calendar_detail(schedule_tab.TAB_ALL.value)
