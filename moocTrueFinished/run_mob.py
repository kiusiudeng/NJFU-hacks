import requests
import json

url = 'https://www.icourse163.org/mob/course/saveContentLearn/v1'

headers = {
    "edu-app-type": "android",
    "mob-token": "",
    "edu-app-version": "3.19.3",
    "edu-app-channel": "ucmooc_store_xiaomi",
    "If-Modified-Since": "Tue, 18 Feb 2020 07:35:59 GMT",
    "device-id": "02:00:00:00:00:00_16DigitsHex",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; MIX Alpha MIUI/20.1.21)",
    "Host": "www.icourse163.org",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Content-Length": "434",
}

body = {
    "mob-token": "HourCookieHere & unitId =  & finished = true &"
}

response = requests.post(url, headers=headers, data=body)
print(response.json())
