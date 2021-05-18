#! /usr/bin/env python3
# coding=utf-8

import requests
from bs4 import BeautifulSoup


def push(title,
         text,
         url='http://libic.njfu.edu.cn/ClientWeb/m/ic2/Default.aspx'):
    """
    赶快在这攒一个企业微信推送吧 -> https://github.com/kiusiudeng/NJFU-hacks/tree/master/WeChatPushforSCF
    不需要推送请直接return
    """
    wx_scf = "https://service-ooacluzp-1251033088.sh.apigw.tencentcs.com/release/wxpush"
    res = requests.get("{}?text={}&desp={}&url={}".format(
        wx_scf, title, text, url)).json()
    if res['errcode'] == 0:
        return


class Occupy:
    """占座操作类"""
    def __init__(self, username, password, seatId):
        self.__username = username
        self.__password = password
        self.__seatId = seatId
        self.__headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://libic.njfu.edu.cn",
            "Referer":
            "http://libic.njfu.edu.cn/ClientWeb/xcus/ic2/Default.aspx",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        self.session = requests.session()
        # 实例化类时就尝试登录保存session
        self.login()

    def login(self):
        """登录"""
        s = self.session.get(
            'http://update.unifound.net/wxnotice/s.aspx?c=100455334_Seat_{}_1CV'
            .format(self.__seatId),
            headers=self.__headers)
        soup = BeautifulSoup(s.content, features="lxml")
        aliUserid = soup.find("input", {"name": "aluseridform"})['value']
        payload = {
            'Dologon': 'true',
            'sysidform': '1CV',
            'aluseridform': aliUserid,
            'szLogonName': self.__username,
            'szPassword': self.__password
        }
        s = self.session.post('http://libic.njfu.edu.cn/Pages/WxSeatSign.aspx',
                              data=payload,
                              headers=self.__headers)
        soup = BeautifulSoup(s.content, features="lxml")
        # print(soup.prettify())
        if soup.body.findAll(text='【 操作成功 】'):
            self.do(int(soup.find("option")['value']) - 1)
            return True
        else:
            push("登录失败！", "请检查用户名密码是否正确！")
            exit(False)

    def do(self, usemin):
        payload = {'DoUserIn': 'true', 'dwUseMin': usemin}
        s = self.session.post('http://libic.njfu.edu.cn/Pages/WxSeatSign.aspx',
                              data=payload,
                              headers=self.__headers)
        soup = BeautifulSoup(s.text, features="lxml")
        push('占座成功！', soup("p")[1].get_text())
        return True


if __name__ == "__main__":
    a = Occupy('1', '1', '10001')
    b = Occupy('2', '2', '10002')
