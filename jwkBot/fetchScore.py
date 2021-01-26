#!/usr/bin/python3

import requests
import hashlib
import time

# 学号密码
stu_id = ''
jwk_pwd = ''


def Run():
    payload = {
        '__VIEWSTATE': '/wEPDwUKLTMzNjY4NzgxOWRkvUsU20I2vYDlxpA1sjoWhQit5wI71Yw2NIm9hDi0zws=',
        '__VIEWSTATEGENERATOR': '56911C19',
        '__EVENTVALIDATION': '/wEdAAIRYxBzHPv4zphuJg7oAk9kZ5IuKWa4Qm28BhxLxh2oFLftNW2DMo/ERJBF+XkFQfVqp4AMzvkUCbvPwTpUGfFr',
        'pcInfo': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36undefined5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36 SN:NULL',
        'txt_mm_expression': '',
        'txt_mm_length': '',
        'txt_mm_userzh': '',
        'typeName': '学生'.encode('gb2312'),
        'dsdsdsdsdxcxdfgfg': hashlib.md5((stu_id+hashlib.md5(jwk_pwd.encode()).hexdigest()[0:30].upper()+'10298').encode()).hexdigest()[0:30].upper(),
        'fgfggfdgtyuuyyuuckjg': '',
        'validcodestate': '0',
        'Sel_Type': 'STU',
        'txt_asmcdefsddsd': stu_id,
        'txt_pewerwedsdfsdff': '',
        'txt_psasas': '请输入密码'.encode('gb2312')
    }

    s = requests.Session()

    # 登录
    s.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        'Referer': 'http://jwk.njfu.edu.cn/_data/login_home.aspx'
    })
    s.post('http://jwk.njfu.edu.cn/_data/login_home.aspx', data=payload)

    # 获取成绩uri
    s.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        'Referer': 'http://jwk.njfu.edu.cn//xscj/Stu_MyScore.aspx'
    })
    # 查询20-21-1学期的成绩，暂时写死
    payload = {'sel_xn': 2020, 'sel_xq': 0, 'SJ': 0, 'btn_search': '检索'.encode('gb2312'),
               'SelXNXQ': 2, 'zfx_flag': 0, 'shownocomputjd': 1, 'zxf': 0, 'hidparam_xh': ''}
    res = s.post(
        'http://jwk.njfu.edu.cn//xscj/Stu_MyScore_rpt.aspx', data=payload)
    h = res.text.find('Stu_MyScore_Drawimg.aspx')
    t = res.text.find('\'', h)

    # 获取成绩jpg
    res = s.get('http://jwk.njfu.edu.cn//xscj/'+res.text[h:t])
    tmp = ''
    try:
        log = open("Score.log", "r")
        tmp = log.read()
    except:
        log = open("Score.log", "w")
        log.write(res.headers['content-length'])
        log.close()
    finally:
        if res.headers['content-length'] == tmp:
            return False
        else:
            log = open("Score.log", "w")
            log.write(res.headers['content-length'])
            log.close()
            with open("Score.jpg", "wb")as f:
                f.write(res.content)
            return True


def push():
    # 方糖Server酱
    requests.post('https://sc.ftqq.com/BLURRRR', data={
                  'text': time.time() + '成绩更新啦！', 'desp': '点此查看:http://139.9.93.236/Score.jpg'})


if __name__ == '__main__':
    if Run():
        push()
    else:
        exit()
