#! /usr/bin/env python3
# coding=utf-8
import arrow
import requests


def push(title, text, url='http://libic.njfu.edu.cn/ClientWeb/m/ic2/Default.aspx'):
    wx_scf = "https://BLUR/"
    res = requests.get("{}?text={}&desp={}&url={}".format(wx_scf, title, text, url)).json()
    if res['errcode'] == 0:
        return


class Reserve:
    """座位操作类"""

    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
                          "X-Requested-With": "XMLHttpRequest",
                          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
                          "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                          "Origin": "http://libic.njfu.edu.cn",
                          "Referer": "http://libic.njfu.edu.cn/ClientWeb/xcus/ic2/Default.aspx",
                          "Accept-Encoding": "gzip, deflate",
                          "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"}
        self.session = requests.session()
        self.login()

    def login(self):
        payload = {"id": self.__username, "pwd": self.__password, "act": "login"}
        time = arrow.now().format("MM-DD HH:mm:ss")
        response = self.session.post("http://libic.njfu.edu.cn/ClientWeb/pro/ajax/login.aspx", data=payload, headers=self.__headers).json()
        if response['ret'] == 1:
            return True
        else:
            push("登录失败！" + time, "请检查用户名密码是否正确！<br>" + response['msg'])
            exit(False)

    def fetch_rsv(self):
        res = self.session.get("http://libic.njfu.edu.cn/ClientWeb/pro/ajax/reserve.aspx?act=get_my_resv").json()
        result = ''
        for p in res['data']:
            result += '座位：{}时间：{}<br>'.format(p['devName'], p['timeDesc'].replace('-', '~').replace('/', '-'))
        return result.rstrip('<br>')

    def reserve(self, dev_id, start, end=""):
        rsv_url = "http://libic.njfu.edu.cn/ClientWeb/pro/ajax/reserve.aspx"
        time = arrow.now()
        start = time.shift(days=+1).format("YYYY-MM-DD " + start)
        if end != '':
            end = time.shift(days=+1).format("YYYY-MM-DD " + end)
        else:
            if time.weekday() == 3:
                end = time.shift(days=+1).format("YYYY-MM-DD " + "20:00")
            else:
                end = time.shift(days=+1).format("YYYY-MM-DD " + "22:00")
        response = self.session.get("{}?dev_id={}&type=dev&start={}&end={}&act=set_resv".format(rsv_url, dev_id, start, end)).json()
        print("{}?dev_id={}&type=dev&start={}&end={}&act=set_resv".format(rsv_url, dev_id, start, end))
        if response['ret'] == 1:
            result = self.fetch_rsv()
            push("预约成功！", result)
            return True
        else:
            result = self.fetch_rsv()
            push('预约失败！', '{}<br>{}'.format(response['msg'], result))
            return False


if __name__ == "__main__":
    a = Reserve('UserName', 'PassWord')
    seats = (100000000, 100000001, 100000002, 100000003)
    for seat in seats:
        if a.reserve(seat, '10:00'):
            break
