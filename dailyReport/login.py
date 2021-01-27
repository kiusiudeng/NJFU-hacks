from aes import aesEnc
import requests
from bs4 import BeautifulSoup
import json

def login(username,password,s):
    headers = {'User-Agent': 'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/88.0.4324.104 safari/537.36',
            'Referer': 'https://ehall.njfu.edu.cn'}

    s.headers.update(headers)
    resp = s.get('https://uia.njfu.edu.cn/authserver/login')
    soup = BeautifulSoup(resp.text, 'lxml')
    lt = soup.select('input[name="lt"]')[0]["value"]
    salt = soup.select('input#pwdDefaultEncryptSalt')[0]['value']

    payload = {'username': username,
            'password': aesEnc(password, salt),
            'lt': lt,
            'dllt': 'userNamePasswordLogin',
            'execution': 'e1s1',
            '_eventId': 'submit',
            'rmShown': '1'}

    s.post('https://uia.njfu.edu.cn/authserver/login',data=payload)
    resp=s.get('http://ehall.njfu.edu.cn/jsonp/getTaskMessageCount')
    try:
        resp=json.loads(resp.text)
        return resp['hasLogin']
    except json.decoder.JSONDecodeError:
        return False