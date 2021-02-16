# -*- coding: utf8 -*-
import json
import requests

# 相关id设置
CORPID = ''  # 企业id
AGENTID = ''  # 应用id
CORPSECRET = ''  # 企业secret

# 企业微信 api url
MSG_URL = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='

# text_card template
text_card_dict = {
    "touser": "@all",
    # "toparty" : "PartyID1 | PartyID2",
    # "totag" : "TagID1 | TagID2",
    "msgtype": "textcard",
    "agentid": AGENTID,
    "textcard": {
        "title": "标题占位",
        "description": "内容占位",
        "url": "URL占位"
    },
    "enable_id_trans": 0,
    "enable_duplicate_check": 0,
    "duplicate_check_interval": 1800
}


def get_access_token():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + CORPID + '&corpsecret=' + CORPSECRET
    resp = requests.get(url=url)
    resp_dict = resp.json()
    access_token = None
    if resp.status_code == 200:
        access_token = resp_dict['access_token']
    return access_token


def main_handler(event, context):
    queryString = event['queryString']
    msg_title = queryString.get('text', None)
    msg_desp = queryString.get('desp', '内容为空')
    msg_url = queryString.get('url', 'http://url')
    text_card_dict['textcard']['title'] = msg_title
    text_card_dict['textcard']['description'] = msg_desp
    text_card_dict['textcard']['url'] = msg_url
    access_token = get_access_token() if msg_title is not None else None
    resp_status = 400
    resp_json = dict()
    if access_token is not None:
        resp = requests.post(url=MSG_URL + access_token, json=text_card_dict)
        resp_status = resp.status_code
        resp_json = resp.json()
    return {
        "isBase64Encoded": False,
        "statusCode": resp_status,
        "headers": {
            'Content-Type': 'application/json'
        },
        "body": json.dumps(resp_json)
    }
