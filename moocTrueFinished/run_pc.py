import requests
import json

url = 'https://www.icourse163.org/web/j/courseBean.saveMocContentLearn.rpc?csrfKey=1b5cb2a1daf84ba59131badbfdd59201'

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
    "Cookie": 'EDUWEBDEVICE=d7852f461faf475fa707807b31f16ebf;__yadk_uid = Zh3BECzeuvQpKjzwNIhgm2CcGRvKt1zT;WM_TID = 8SdfprdzngBFVQRQQEZ7BLQNrwOnwMOl;NTES_PASSPORT = MTRyh4_O6sLFXT7KlPWBTH9sYBFl.mNJfiDInsq3OC3iNc6hHt_Vu36H0U2_1QPzCtyXvFff4pkToljTGLYcY1WaN28pl4LvfqHMG.zMdszmcQ9XsUu6ivaBvKmpjnuPIZmvU08mIk74MeTLQpZutL_OXTH6w.9CAOO02O7eFBU19U40Y91GD0r3X;P_INFO = king6556@163.com | 1583818597 | 1 | imooc | 11 & 5 | jis & 1583340204 & cloudmusic  # jis&320300#10#0#0|&0|edumooc_client&cloudmusic|king6556@163.com; hasVolume=true; videoRate=1.25; videoResolutionType=3; videoVolume=1; NTESSTUDYSI=1b5cb2a1daf84ba59131badbfdd59201; STUDY_INFO="king6556@163.com|-1|1965489|1584508984028"; STUDY_SESS="dhyMAJPZOPpWS1O/6pDzpgtKX4d2maayKCHWY572cnB/+ySjM0rkFiPypmELfWZnn2g/3+o43M+2nf23NcOL1AbrR5fYcu+WaTbyBAibWi2V+hD8Cc7W3OMuxykulvOtYP7/RGtBo6bB8nYabSI7tzb5+n54rjK6ejB9QXEN6A+tHU1zgSEwLkSDa3nJLvx+"; STUDY_PERSIST="5jvJhYwkCwNF9Un6dxAvH/XR3tb3FC8x0n1Ce73EYdZGmQE9V2ZoluF7DjvPwuyAZKmoYxcnO20x2gkt39EFHc6LQHWjrSz+m1T6kFt5BZ0tBafPkhGr0chnm2iayKaPl1Jp/iZyR4obESVapRPOy1U50ItzPSebQI4Gc/hLrL81UHSFBCH0wQpRKhOnXE3MzLiqH3b5yw2VDa14HCTv1PfjbuhHrFAzCWQB41FFH6iRbRfxmR1FpmJxCYfcl2LM8WQLi3xTJ45sq/acjsEWiA=="; NETEASE_WDA_UID=1965489#|#1402316854165; WM_NI=adAlAETyYh56ZB%2FXEEFySav1FENCax5bzd%2BWsGlXr4wSEOcBWIYZiEGLn58IJNai%2Ffj%2F1fqIPNyv8o1Ig9HgpGo1LX%2Bcii4Ef7rg6STmHMtREamq1QJZSJ7gBHdjBxGlQ1c%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8ff14eaeb7a083bc21e9b88ea3d85e939a8aabb65ea6a7a9b7b74ab8ba8796fc2af0fea7c3b92aa3bc8f8dc44f98a79789b83e9a9ee1b9c84f86a79d82f53b869b82a4e474f7beb685aa5db199a4b9f140b58d8bb0e24a959797bbec4f8594a2d6bb438a92af8aae6eaaf1ff87f4439492b797bb65f397a9dacb6db499a1d2cf54e9bda78ab74fa6e9be88b55998b388aef75a87bfa392b45b8a869dabb66d8298ac8bc17485b49fd2e237e2a3;'
}

for id in range(1224452981, 1224452997):
    body = {
        'dto': json.dumps({
            "unitId": id,
            "finished": "true"})
    }
    response = requests.post(url, headers=headers, data=body)
    print(response.json())
