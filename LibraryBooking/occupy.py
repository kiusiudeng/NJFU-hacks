#! /usr/bin/env python3
# coding=utf-8

import requests
from bs4 import BeautifulSoup

id = '18508'
pwd = 'Q'
session = requests.session()
s = session.get(
    'http://update.unifound.net/wxnotice/s.aspx?c=100455334_Seat_100456256_1CV'
)
soup = BeautifulSoup(s.text, features="lxml")
aliUserid = soup.find("input", {"name": "aluseridform"})['value']
payload = {
    'Dologon': 'true',
    'sysidform': '1CV',
    'aluseridform': aliUserid,
    'szLogonName': id,
    'szPassword': pwd
}
s = session.post('http://libic.njfu.edu.cn/Pages/WxSeatSign.aspx',
                 data=payload)
usemin = 100
payload = {'DoUserIn': 'true', 'dwUseMin': usemin}
print(s.text)