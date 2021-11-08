#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/9/14 13:20
# @Author   : 蓦然
# @File     : candidate_enumerate.py
# Project   : ATS

import time
from pprint import pprint
from faker import Faker
from test_case.common import request
from test_case.enumeration_ats.candidate_enumerate import candidate_status
from test_config import param_config

fake = Faker(locale='zh_CN')


def candidate_page(name=None, phone=None):
    """
    分页查询候选人列表
    :param name:
    :param phone:
    :return:
    """
    url = '/pic/api/candidate/page'
    body = {
        "actualEntryTimeEnd": None,
        "actualEntryTimeStart": None,
        "ageEnd": None,
        "ageStart": None,
        "channelId": None,
        "createTimeEnd": None,
        "createTimeStart": None,
        "createrEwId": None,
        "education": None,
        "gender": None,
        "hrEwId": None,
        "interviewTimeEnd": None,
        "interviewTimeStart": None,
        "nameOrPhone": name,
        "pageNum": 1,
        "pageSize": 20,
        "planEntryTimeEnd": None,
        "planEntryTimeStart": None,
        "positionId": None,
        "tagIds": [],
        "workYearsEnd": None,
        "workYearsStart": None,
        "expectCity": None
    }
    response = request.post_body(url, body)
    candidatename = ''
    candidatephone = ''
    id = ''
    for candidate in response['data']['records']:
        if candidate['name'] == name or candidate['phone'] == phone:
            candidatename = candidate['name']
            candidatephone = candidate['phone']
            id = candidate['id']
    return id, candidatename, candidatephone


def candidate_create(name, phone=param_config.phone, channelId='161362469970203', positionId='162865242215821'):
    """
    创建候选人
    :param name:
    :param phone:
    :param channelId:
    :param positionId:
    :return:
    """
    # global status
    url = '/pic/api/candidate/create'
    body = {
        "channelId": channelId,
        "channelName": "",
        "passFlag": 0,
        "positionId": positionId,
        "resumeBasicInfoVO": {
            "age": "30",
            "currentAddress": "上海浦东新区",
            "currentWorkStatus": 1,
            "dutyTime": "十天",
            "education": None,
            "email": "m17600888399@163.com",
            "expectCity": "北京/北京市/东城区",
            "expectIndustry": "软件",
            "expectPosition": "软件测试",
            "expectSalary": "20000",
            "gender": 1,
            "graduatedSchool": "",
            "name": name,
            "phone": phone,
            "profession": "",
            "selfEvaluation": "良好",
            "skill": "1",
            "workYears": 8
        },
        "status": 10,
        "workExperienceVOS": [{
            "beginDate": "2014-08",
            "endDate": "至今",
            "leaveReason": "个人原因",
            "position": "java开发",
            "workCompany": "软通动力",
            "workContent": "1",
            "workResult": "1"
        }],
        "educationVOS": [{
            "beginDate": "2010-09",
            "education": 6,
            "endDate": "2014-07",
            "profession": "中文",
            "school": "浙江大学"
        }],
        "projectVOS": [{
            "beginDate": "2014-08",
            "endDate": "至今",
            "projectDescription": "1",
            "projectDuty": "1",
            "projectName": "喔趣企管",
            "projectPerformance": "1",
            "projectRole": "java开发"
        }],
        "workSkillVOS": [{
            "level": "1",
            "name": "1"
        }],
        "tags": []
    }
    request.post_body(url, body=body)
    page_url = '/pic/api/candidate/page'
    page_body = {
        "actualEntryTimeEnd": None,
        "actualEntryTimeStart": None,
        "ageEnd": None,
        "ageStart": None,
        "channelId": None,
        "createTimeEnd": None,
        "createTimeStart": None,
        "createrEwId": None,
        "education": None,
        "gender": None,
        "hrEwId": None,
        "interviewTimeEnd": None,
        "interviewTimeStart": None,
        "pageNum": 1,
        "pageSize": 20,
        "planEntryTimeEnd": None,
        "planEntryTimeStart": None,
        "positionId": None,
        "tagIds": [],
        "workYearsEnd": None,
        "workYearsStart": None,
        "expectCity": None
    }
    page_response = request.post_body(page_url, page_body)
    # print(page_response['code'])
    uid = ""
    status = ""
    for pagelist in page_response['data']['records']:
        if pagelist['name'] == name:
            uid = pagelist['id']
            if pagelist['status'] == candidate_status.WAIT_FOR_SCREEN.value:
                status = pagelist['status']
            else:
                raise Exception('候选人状态错误筛选通过失败')
        break
    rl = [name, uid, status, channelId, positionId]
    return rl


def candidate_detail(candidateId):
    """
    查询候选人详情
    :param candidateId:
    :return:
    """
    url = '/pic/api/candidate_resume/resume_detail?candidateId={cid}'.format(cid=candidateId)
    response = request.get(url)
    # print(response)
    return response['data']['candidateResume']


def delete_candidate(candidateId):
    """
    候选人删除
    :param candidateId:
    :return:
    """
    url = '/pic/api/candidate/delete_candidate?candidateId={id}'.format(id=candidateId)
    request.get(url)


def update_candidate_status(name, uid, status):
    """
    更改状态
    :param name:
    :param uid:
    :param status: 状态 0-初筛淘汰或面试淘汰 10-待筛选 20-筛选通过 30-已安排面试 40-已面试 50-拟录用 60-待入职 70-已入职
    :return:
    """
    url = '/pic/api/candidate/update_candidate_status'
    body = {
        "status": status,
        "name": name,
        "candidateId": uid,
        "passFlag": None,
        "candidateIdSet": [uid]
    }
    response = request.post_body(url, body)


def interview_create(uid):
    """
    安排面试
    :param uid:
    :return:
    """
    url = '/pic/api/candidate/interview/create'
    body = {
        "addressHouseNumber": "A栋2楼202",
        "attachmentUrlList": [],
        "candidateId": uid,
        "conferenceRoomName": "后裔会议室",
        "contactName": "莫金龙",
        "contactPhone": "17600888399",
        "email": "m17600888399@163.com",
        "emailCc": "",
        "emailNotifyOriginalTemplate": "<h2 style=\"text-align:center;\">面试通知</h2>\n<p>尊敬的 <span style=\"color: "
                                       "#0074ff;\">#候选人姓名#</span></p>\n<p style=\"text-indent: 2em;\">您好，感谢您对 <span "
                                       "style=\"color: #0074ff;\">#公司名称#</span> "
                                       "的信任和支持，您提供的应聘资料符合我司的面试要求，特邀您前来参与面试。为能顺利帮您安排面试，请详细了解以下信息：</p>\n<p>应聘职位：&nbsp"
                                       ";<span style=\"color: rgb(0, 116, "
                                       "255);\">#应聘职位#</span>&nbsp;</p>\n<p>面试时间：<span style=\"color: "
                                       "#0074ff;\">#面试时间#</span></p>\n<p>面试地址：<span style=\"color: "
                                       "#0074ff;\">#面试地址#</span></p>\n<p style=\"text-indent: "
                                       "2em;\">请您安排时间准时到达面试地点，如有问题请与 <span style=\"color: #0074ff;\">#联系人#</span>（ "
                                       "<span style=\"color: #0074ff;\">#联系人电话#</span> ）联系。</p>\n<p>祝您面试成功,袁帅测试</p>",
        "emailTitle": "【喔趣企业管理】面试邀请",
        "hrEwId": "MoJinLong",
        "interviewAddress": "上海市徐汇区斜土路2899号(近星游城)",
        "interviewAddressLat": 31.185694,
        "interviewAddressLng": 121.441156,
        "interviewEndTime": int(time.time() * 1000) + 1000000,
        "interviewTime": int(time.time() * 1000),
        "interviewerEwIds": ["MoJinLong"],
        "method": 0,
        "notifyCandidateMethods": [2],
        "notifyInterviewerMethods": [1],
        "positionId": "162865242215821",
        "addressShort": "光启文化广场",
        "regional": "上海市",
        "replyEmail": "",
        "corpNotifyTemplateId": "32127554227933184",
        "emailNotifyTemplate": "<h2 style=\"text-align:center;\">面试通知</h2>\n<p>尊敬的 <span style=\"color: "
                               "#0074ff;\">张三</span></p>\n<p style=\"text-indent: 2em;\">您好，感谢您对 <span style=\"color: "
                               "#0074ff;\">喔趣企业管理</span> "
                               "的信任和支持，您提供的应聘资料符合我司的面试要求，特邀您前来参与面试。为能顺利帮您安排面试，请详细了解以下信息：</p>\n<p>应聘职位：&nbsp;<span "
                               "style=\"color: rgb(0, 116, 255);\">测试</span>&nbsp;</p>\n<p>面试时间：<span style=\"color: "
                               "#0074ff;\">2021-09-14 10:45-11:00</span></p>\n<p>面试地址：<span style=\"color: "
                               "#0074ff;\">上海市徐汇区斜土路2899号(近星游城)A栋2楼202</span></p>\n<p style=\"text-indent: "
                               "2em;\">请您安排时间准时到达面试地点，如有问题请与 <span style=\"color: #0074ff;\">测试联系人张三</span>（ <span "
                               "style=\"color: #0074ff;\">166-0124-5399</span> ）联系。</p>\n<p>祝您面试成功,袁帅测试</p> "
    }
    response = request.post_body(url, body)


def add_candidate_tag():
    """
    给候选人添加标签
    post
        candidateId
        name
    """
    url = '/pic/api/candidate/add_candidate_tag'


def add_evaluation():
    """
    添加候选人评价
    """


def candidate_dynamics_page():
    """
    分页查询候选人动态
    """


def candidate_interview_page():
    """
    面试记录
    """


def candidate_offer_page():
    """
    offer记录
    """


def candidate_participant_list():
    """
    查询招聘参与者列表
    """


def chatInfo():
    """
    获取会话信息
    """


def check_in_process():
    """
    检查当前手机号候选人是否在流程中
    """


def countStatus():
    """
    候选人分页状态统计
    """


def delete_candidate_tag():
    """
    删除候选人标签
    """


def delete_evaluation():
    """
    删除评价
    """


def edit_resume():
    """
    编辑简历
    """


def eliminate():
    """
    淘汰
    """


def emailParserAddCandidate():
    """
    邮箱导入-解析添加候选人
    """


def evaluation_detail():
    """
    查看评价
    """


def evaluation_recode_page():
    """
    分页查询候选人评价
    """


def get_eliminate_reason():
    """
    查看淘汰原因
    """


def get_record_num():
    """
    获取每个记录的数量
    """


def offer_detail():
    """
    查看offer
    """


def page():
    """
    候选人分页查询
    """


def saveChatInfo():
    """
    保存会话信息
    """


def share_dynamics():
    """
    分享后加入动态
    """


def update_channel():
    """
    修改候选人招聘渠道
    """


def update_phone():
    """
    更改手机号
    """


def update_position():
    """
    修改候选人招聘职位
    """


def get_position_by_id():
    """
    根据id查询职位
    """


def reSumParser(file_name):
    """"
    简历解析: k18
    file name : file
    """
    url = '/pic/api/candidate_resume/resumeParser'
    response = request.post_file(url, file_name=file_name)
    print(response)
    return response

# 候选人-offer


# --------- 背调 -------
def back_tone_order_create(amount, candidateId, candidateIdCard, candidateName, candidatePhoneNo, clientContact,
                           clientEmail, clientPhoneNo, email, itemList, position, productId, productName,
                           flag, department=None, companyName=None, itemCode=None, itemName=None, perfNum=None,
                           witnessNum=None, xpNum=None):
    """
    创建背调订单
    request: POST
            参数名称  			参数说明  		    是否必须    数据类型
            submitRequest		订单提交				true
            amount				套餐金额				false	   string
            candidateId			候选人id				false	   integer(int64)
            candidateIdCard		候选人身份证号		false	   string
            candidateName		候选人姓名			false	   string
            candidatePhoneNo	候选人手机号			false	   string
            clientContact		委托方联系人			false	   string
            clientPhoneNo		委托方联系电话		false	   string
            itemList			背调数据项列表		false	   array
            companyName			公司名称				false	   string
            itemCode			数据项code			false	   string
            itemName			数据项名称			false	   string
            perfNum				工作经历之表现个数	false	   integer
            witnessNum			证明人数量			false	   integer
            xpNum				工作经历之履历个数	false	   integer
            productId			套餐id				false	   string
            productName			套餐名称				false	   string
    """

    body = {
        "amount": amount,  # 套餐金额
        "candidateId": candidateId,  # 候选人id
        "candidateIdCard": candidateIdCard,  # 候选人身份证号
        "candidateName": candidateName,  # 候选人名称
        "candidatePhoneNo": candidatePhoneNo,  # 候选人phone
        "clientContact": clientContact,  # 委托方name
        "clientEmail": clientEmail,  # 委托方emaill
        "clientPhoneNo": clientPhoneNo,  # 委托方电话
        "department": department,  # 部门
        "email": email,  # 候选人emaill
        "position": position,  # 职位
        "productId": productId,  # 部门id
        "productName": productName,  # 套餐id
        "flag": flag,
        "expanded": False,
        "itemList": itemList,  # 背调套餐内容列表
    }
    url = '/pic/api/candidate/back_tone_order/create'
    response = request.post_body(url, body=body)
    print(response)


def back_tone_order_cancel(orderNo):
    """
    取消订单
    request : POST
    params : orderNo
    参数名称   是否必须    数据类型
    orderNo   true      string
    """
    url = '/pic/api/candidate/back_tone_order?cancel={orderNo}'.format(orderNo=orderNo)
    request.post(url)


def back_tone_order_delete(Id):
    """
    删除订单
    request : post
    params : id
    参数名称    参数说明    是否必须    数据类型
    id         订单id     true       integer
    """
    url = '/pic/api/candidate/back_tone_order/delete={Id}'.format(Id=Id)
    assert Id != '' and Id is not None
    request.post(url)
    pass


def back_tone_order_list(candidateId):
    """
    背调订单列表
    request : post
    params : candidateId
    参数名称    参数说明    是否必须    数据类型
    candidateId          true       integer
    """
    url = '/pic/api/candidate/back_tone_order/list?candidateId={candidateId}'.format(candidateId=candidateId)
    assert candidateId != '' and candidateId is not None
    response = request.post(url)
    # assert response['code'] != ""
    orderNolist = []
    # print(response)
    for order in response['data']:
        orderNolist.append(order['orderNo'])
        print("背调订单号:", orderNolist)
    return response


def back_tone_order_open(ewUserId, corpId=0):
    """"
    开通背调
    request : post
    parameter
    参数名称     参数说明    是否必须    数据类型
    corpId	   企业客户id   false     integer
    ewUserId   企业微信ID   false     string
    """
    url = '/pic/api/candidate/back_tone_order/open'
    body = {
        "corpId": corpId,
        "ewUserId": ewUserId
    }
    response = request.post_body(url, body=body)
    return response
    # assert response['code'] != ""


def back_tone_order_open_flag():
    """
    是否开通背调
    request : post
    """
    url = '/pic/api/candidate/back_tone_order/open_flag'
    response = request.post(url)
    # print(url+'是否开通背调')
    pprint(response)
    return response


def back_tone_order_view(orderNo=0):
    """
    查看报告
    params : orderNo
    参数名称    参数说明    是否必须    数据类型
    orderNo   orderNo    true      integer
    """
    url = '/pic/api/candidate/back_tone_order/view/{orderNo}'.format(orderNo=orderNo)
    response = request.post(url)
    print(response)
    return response


def back_tone_order_choose_package(productName):
    """
    查询套餐
    request : post
    """
    url = '/pic/api/candidate/back_tone_order/choose_package'
    response = request.post(url)
    packAge = response['data']['groupList']
    packageList = []
    for x in packAge:
        if productName == x['productName']:
            packageList = x
    return packageList


def attachment():
    """
    :return:
    """
    url = '/pic/api/candidate/attachment/create'
    body = {
        "name": "_【前端开发工程 师 】丁琪 6年 - ",
        "type": 50,
        "size": 2516205,
        "attachmentUrl": "https://ats-test-bucket-1304887218.cos.ap-shanghai.myqcloud.com/file/202110/26"
                         "/EiQSoFs6LSGJIdrLHE5Z6.pdf",
        "candidateId": "163522005505570"
    }
    response = request.post_body(url, body=body)


if __name__ == '__main__':
    # '''创建候选人:待筛选-筛选通过'''
    candidate_enumerates = candidate_status
    create = candidate_create(name=fake.name())
    if create[2] == candidate_enumerates.WAIT_FOR_SCREEN.value:
        update_candidate_status(name=create[0], uid=create[1], status=candidate_enumerates.SUCCESS_SCREEN.value)
    else:
        raise Exception('候选人{}状态错误'.format(create[0]))
    ''' 安排面试'''
    interview_create(uid=create[1])
    update_candidate_status(name=create[0], uid=create[1], status=candidate_enumerates.SUCCESS_SCHEDULED.value)
    # back_tone_order_open_flag()
    # # 背调套餐查询
    # package = back_tone_order_choose_package("套餐A")
    # # 发起背调
    # id = candidate_page(name=create[0], phone=None)[0]
    # candidate_detail(candidateId=id)
    # back_tone_order_create(amount=package['amount'], candidateId=id, candidateIdCard=None, candidateName=create[0],
    #                        candidatePhoneNo=param_config.phone, clientContact=param_config.clientContact,
    #                        clientEmail=param_config.email, clientPhoneNo=param_config.phone, department=None,
    #                        email=param_config.email, itemList=package['itemList'], position="测试",
    #                        flag=package['flag'], productId=package['productId'], productName=package['productName'])
    # back_tone_order_list(id)
    # ===========================================
# ____________
# back_tone_order_list()
# back_tone_order_create()
# file_name = '【测试工程师  _ 上海12-18K】高杰 12年.pdf'
# reSumParser(file_name)
# interview_create(create[1], 1631624188000)
# delete_candidate(cid=create[1])
