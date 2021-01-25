import requests
import json

xiqueURL = "http://api.xiqueer.com/manager//wap/wapController.jsp"
payload = {'encrptSecretKey': '',
           'param': '',
           'xqerSign': '',
           'appinfo': 'android2.6.303',
           'echo': '',
           'param2': '',
           'timestamp': 1611570092,
           'token': ''}
headers = {'user-agent': 'okhttp/3.10.0'}

res = requests.post(url=xiqueURL, headers=headers, data=payload)
res = json.loads(res.text)
res = res['xscj']
for p in res:
    print(p['kcmc']+':'+p['kscjm'])
