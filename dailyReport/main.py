from login import login
import requests
import json
import time
import sys

# uia账号密码配置
stu_id = ''
password = ''
sckey = ''  # 留空表示禁用消息推送


def push(msg):
    if sckey == '':
        return
    else:
        requests.post('https://sc.ftqq.com/'+sckey + '.send?text='+msg)


def checkin(s):
    s.get('http://ehall.njfu.edu.cn/qljfwapp/sys/lwNjfuStudentEpidemic/index.do')
    resp = s.post(
        'http://ehall.njfu.edu.cn/qljfwapp/sys/lwNjfuStudentEpidemic/modules/application/getTodayHasReported.do')
    resp = json.loads(resp.text)
    if resp['datas']['getTodayHasReported']['totalSize'] == 0:
        resp = s.post(
            'http://ehall.njfu.edu.cn/qljfwapp/sys/lwNjfuStudentEpidemic/modules/application/getMyTodayReportWid.do')
        resp = json.loads(resp.text)['datas']['getMyTodayReportWid']['rows'][0]
        payload = {}
        payload['WID'] = resp['WID']
        payload['USER_ID'] = resp['USER_ID']
        payload['USER_NAME'] = resp['USER_NAME']
        payload['GENDER_CODE'] = resp['GENDER_CODE']
        payload['CAMPUS_CODE'] = resp['CAMPUS_CODE']
        payload['COLLEGE_CODE'] = resp['COLLEGE_CODE']
        payload['COLLEGE_NAME'] = resp['COLLEGE_NAME']
        payload['DEPT_CODE'] = resp['DEPT_CODE']
        payload['DEPT_NAME'] = resp['DEPT_NAME']
        payload['CAMPUS_NAME'] = resp['CAMPUS_NAME']
        payload['PHONE_NUMBER'] = resp['PHONE_NUMBER']
        payload['IDCARD_NO'] = resp['IDCARD_NO']
        payload['NEED_CHECKIN_DATE'] = resp['NEED_CHECKIN_DATE']
        resp = s.post(
            'http://ehall.njfu.edu.cn/qljfwapp/sys/lwNjfuStudentEpidemic/modules/application/getLatestDailyReportData.do')
        resp = json.loads(resp.text)[
            'datas']['getLatestDailyReportData']['rows'][0]
        payload['HEALTH_STATUS_CODE_DISPLAY'] = resp['HEALTH_STATUS_CODE_DISPLAY']
        payload['HEALTH_STATUS_CODE'] = resp['HEALTH_STATUS_CODE']
        payload['HEALTH_MORNING_CODE_DISPLAY'] = resp['HEALTH_MORNING_CODE_DISPLAY']
        payload['HEALTH_MORNING_CODE'] = resp['HEALTH_MORNING_CODE']
        payload['HEALTH_LUNCH_CODE_DISPLAY'] = resp['HEALTH_LUNCH_CODE_DISPLAY']
        payload['HEALTH_LUNCH_CODE'] = resp['HEALTH_LUNCH_CODE']
        payload['LIVE_IN_SCHOOL'] = resp['LIVE_IN_SCHOOL']
        payload['IS_LIVE_EPIDEMIC_DISPLAY'] = resp['IS_LIVE_EPIDEMIC_DISPLAY']
        payload['IS_LIVE_EPIDEMIC'] = resp['IS_LIVE_EPIDEMIC']
        payload['IS_HAPPEND_UNUSUAL_DISPLAY'] = resp['IS_HAPPEND_UNUSUAL_DISPLAY']
        payload['IS_HAPPEND_UNUSUAL'] = resp['IS_HAPPEND_UNUSUAL']
        payload['CHECKED_DISPLAY'] = resp['CHECKED_DISPLAY']
        payload['CHECKED'] = resp['CHECKED']
        payload['CZR'] = resp['CZR']
        payload['CZZXM'] = resp['CZZXM']
        payload['CZRQ'] = resp['CZRQ']
        payload['CREATED_AT'] = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime())
        s.post('http://ehall.njfu.edu.cn/qljfwapp/sys/lwNjfuStudentEpidemic/modules/application/T_STUDENT_EPIDEMIC_CHECKIN_SAVE.do', data=payload)

        resp = s.post(
            'http://ehall.njfu.edu.cn/qljfwapp/sys/lwNjfuStudentEpidemic/modules/application/getTodayHasReported.do')
        resp = json.loads(resp.text)
        if resp['datas']['getTodayHasReported']['totalSize'] == 1:
            push("今日已打卡成功！")
            exit()
    else:
        push("今日已打卡，程序已结束运行。")
        exit()


if __name__ == '__main__':
    s = requests.session()
    try:
        if login(stu_id, password, s):
            checkin(s)
            exit()
        else:
            push("登录失败！可能是账号密码错误，或出现验证码导致。")
            exit()
    except Exception:
        push("每日打卡程序运行时发生了错误。")
        exit()
