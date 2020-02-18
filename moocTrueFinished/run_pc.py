import requests
import json

url = 'https://www.icourse163.org/web/j/courseBean.saveMocContentLearn.rpc?csrfKey='

headers = {
    "Host": "www.icourse163.org",
    "Connection": "keep-alive",
    "Content-Length": "57",
    "Sec-Fetch-Dest": "empty",
    "edu-script-token": "",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",
    "DNT": "1",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "*/*",
    "Origin": "https://www.icourse163.org",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Referer": "https://www.icourse163.org",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": 'EDUWEBDEVICE=; NTES_PASSPORT=; P_INFO=; NTESSTUDYSI=; STUDY_INFO=""; STUDY_SESS=""; STUDY_PERSIST=""; NETEASE_WDA_UID=; WM_NI=; WM_NIKE=; WM_TID=; hasVolume=true; videoVolume=1; MOOC_PRIVACY_INFO_APPROVED=true; bpmns=1;videoResolutionType=3; videoRate=1; '
}

body = {
    'dto': json.dumps({
        "unitId": "",
        "finished": "true"})
}

response = requests.post(url, headers=headers, data=body)
print(response.json())
