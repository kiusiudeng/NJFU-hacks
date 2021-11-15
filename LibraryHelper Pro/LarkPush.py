import json
import requests


class LarkPush:
    botUrl = "此处填写你的飞书自定义机器人URL"

    def pushText(self, text):
        data = {'msg_type': "text"}
        content = {'text': text}
        data['content'] = content
        # 发送POST请求
        res = requests.post(url=self.botUrl, data=json.dumps(data))
        print(res.text)

    def pushBookSuccess(self, studentID, position, startTime, endTime):
        data = {'msg_type': "interactive"}
        card = {
            "elements": [
                {
                    "fields": [
                        {
                            "is_short": True,
                            "text": {
                                "content": '**👤 学号：**\n' + studentID,
                                "tag": "lark_md"
                            }
                        },
                        {
                            "is_short": True,
                            "text": {
                                "content": '**🪑 座位：**\n' + position,
                                "tag": "lark_md"
                            }
                        },
                        {
                            "is_short": False,
                            "text": {
                                "content": "",
                                "tag": "lark_md"
                            }
                        },
                        {
                            "is_short": True,
                            "text": {
                                "content": '**🕐 开始时间：**\n' + startTime,
                                "tag": "lark_md"
                            }
                        },
                        {
                            "is_short": True,
                            "text": {
                                "content": '**🕐 结束时间：**\n' + endTime,
                                "tag": "lark_md"
                            }
                        }
                    ],
                    "tag": "div"
                },
                {
                    "actions": [
                        {
                            "tag": "button",
                            "text": {
                                "content": "查看所有预约",
                                "tag": "plain_text"
                            },
                            "type": "primary",
                            "url": "http://libic.njfu.edu.cn/clientweb/"
                        }
                    ],
                    "tag": "action"
                }
            ],
            "header": {
                "template": "green",
                "title": {
                    "content": "👍【预约成功】",
                    "tag": "plain_text"
                }
            }
        }
        data['card'] = card
        # 发送POST请求
        res = requests.post(url=self.botUrl, data=json.dumps(data))
        print(res.text)
