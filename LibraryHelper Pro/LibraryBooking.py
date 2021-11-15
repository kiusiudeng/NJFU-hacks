import traceback

import requests
import json
import LarkPush

roomInfo = [{"id": "100455356", "title": None, "name": "四层A区", "roomName": None, "devNum": None, "kindId": None,
             "kindName": None, "labName": "图书馆四层", "labId": "100455336", "state": None, "prop": None, "openTimes": None,
             "rsvs": None, "roomStat": {"dwRoomID": 100455356, "szRoomName": "四层A区", "szRoomNo": "7", "szFloorNo": "",
                                        "dwOpenBegin": 700, "dwOpenEnd": 2200, "dwTotalNum": None, "dwUsableNum": None,
                                        "szMemo": None}},
            {"id": "100455344", "title": None, "name": "二层A区", "roomName": None, "devNum": None, "kindId": None,
             "kindName": None, "labName": "图书馆二层", "labId": "100455331", "state": None, "prop": None, "openTimes": None,
             "rsvs": None, "roomStat": {"dwRoomID": 100455344, "szRoomName": "二层A区", "szRoomNo": "1", "szFloorNo": "",
                                        "dwOpenBegin": 700, "dwOpenEnd": 2200, "dwTotalNum": None, "dwUsableNum": None,
                                        "szMemo": None}},
            {"id": "100455346", "title": None, "name": "二层B区", "roomName": None, "devNum": None, "kindId": None,
             "kindName": None, "labName": "图书馆二层", "labId": "100455331", "state": None, "prop": None, "openTimes": None,
             "rsvs": None, "roomStat": {"dwRoomID": 100455346, "szRoomName": "二层B区", "szRoomNo": "2", "szFloorNo": "",
                                        "dwOpenBegin": 700, "dwOpenEnd": 2200, "dwTotalNum": None, "dwUsableNum": None,
                                        "szMemo": None}},
            {"id": "100455350", "title": None, "name": "三层A区", "roomName": None, "devNum": None, "kindId": None,
             "kindName": None, "labName": "图书馆三层", "labId": "100455334", "state": None, "prop": None, "openTimes": None,
             "rsvs": None, "roomStat": {"dwRoomID": 100455350, "szRoomName": "三层A区", "szRoomNo": "4", "szFloorNo": "",
                                        "dwOpenBegin": 700, "dwOpenEnd": 2200, "dwTotalNum": None, "dwUsableNum": None,
                                        "szMemo": None}},
            {"id": "100455352", "title": None, "name": "三层B区", "roomName": None, "devNum": None, "kindId": None,
             "kindName": None, "labName": "图书馆三层", "labId": "100455334", "state": None, "prop": None, "openTimes": None,
             "rsvs": None, "roomStat": {"dwRoomID": 100455352, "szRoomName": "三层B区", "szRoomNo": "5", "szFloorNo": "",
                                        "dwOpenBegin": 700, "dwOpenEnd": 2200, "dwTotalNum": None, "dwUsableNum": None,
                                        "szMemo": None}},
            {"id": "100455354", "title": None, "name": "三层C区", "roomName": None, "devNum": None, "kindId": None,
             "kindName": None, "labName": "图书馆三层", "labId": "100455334", "state": None, "prop": None, "openTimes": None,
             "rsvs": None, "roomStat": {"dwRoomID": 100455354, "szRoomName": "三层C区", "szRoomNo": "6", "szFloorNo": "",
                                        "dwOpenBegin": 700, "dwOpenEnd": 2200, "dwTotalNum": None, "dwUsableNum": None,
                                        "szMemo": None}},
            {"id": "100455358", "title": None, "name": "五层A区", "roomName": None, "devNum": None, "kindId": None,
             "kindName": None, "labName": "图书馆五层", "labId": "100455338", "state": None, "prop": None, "openTimes": None,
             "rsvs": None, "roomStat": {"dwRoomID": 100455358, "szRoomName": "五层A区", "szRoomNo": "8", "szFloorNo": "",
                                        "dwOpenBegin": 700, "dwOpenEnd": 2200, "dwTotalNum": None, "dwUsableNum": None,
                                        "szMemo": None}},
            {"id": "100455360", "title": None, "name": "六层", "roomName": None, "devNum": None, "kindId": None,
             "kindName": None, "labName": "图书馆六层", "labId": "100455342", "state": None, "prop": None, "openTimes": None,
             "rsvs": None,
             "roomStat": {"dwRoomID": 100455360, "szRoomName": "六层", "szRoomNo": "9", "szFloorNo": "",
                          "dwOpenBegin": 700,
                          "dwOpenEnd": 2200, "dwTotalNum": None, "dwUsableNum": None, "szMemo": None}},
            {"id": "106658017", "title": None, "name": "七层北侧", "roomName": None, "devNum": None, "kindId": None,
             "kindName": None, "labName": "图书馆七层", "labId": "106657931", "state": None, "prop": None, "openTimes": None,
             "rsvs": None, "roomStat": {"dwRoomID": 106658017, "szRoomName": "七层北侧", "szRoomNo": "10", "szFloorNo": "",
                                        "dwOpenBegin": 700, "dwOpenEnd": 2200, "dwTotalNum": None, "dwUsableNum": None,
                                        "szMemo": None}},
            {"id": "111488386", "title": None, "name": "三楼夹层", "roomName": None, "devNum": None, "kindId": None,
             "kindName": None, "labName": "图书馆三楼夹层", "labId": "111488380", "state": None, "prop": None,
             "openTimes": None,
             "rsvs": None, "roomStat": {"dwRoomID": 111488386, "szRoomName": "三楼夹层", "szRoomNo": "11", "szFloorNo": "",
                                        "dwOpenBegin": 700, "dwOpenEnd": 2200, "dwTotalNum": None, "dwUsableNum": None,
                                        "szMemo": None}},
            {"id": "111488388", "title": None, "name": "四楼夹层", "roomName": None, "devNum": None, "kindId": None,
             "kindName": None, "labName": "图书馆四楼夹层", "labId": "111488382", "state": None, "prop": None,
             "openTimes": None,
             "rsvs": None, "roomStat": {"dwRoomID": 111488388, "szRoomName": "四楼夹层", "szRoomNo": "12", "szFloorNo": "",
                                        "dwOpenBegin": 700, "dwOpenEnd": 2200, "dwTotalNum": None, "dwUsableNum": None,
                                        "szMemo": None}}]


class LibraryBooking:
    libUrl = "http://libic.njfu.edu.cn/ClientWeb/"
    larkPush = LarkPush.LarkPush()

    def login(self, stuID, passwd):
        loginUrl = self.libUrl + "pro/ajax/login.aspx"
        param = {"act": "login", "id": stuID, "pwd": passwd, "role": "512"}

        try:
            res = requests.post(url=loginUrl, params=param)
            print(res.text)
            if json.loads(res.text).get('msg') != 'ok':
                return
            cookies = res.cookies
            cookie = requests.utils.dict_from_cookiejar(cookies)
            return cookie
        except Exception as err:
            print('获取cookie失败：\n{0}'.format(err))

    def fetchAvailableSeatsByRoom(self, room_id, date, fr_start, fr_end):
        fetchUrl = self.libUrl + "pro/ajax/device.aspx"

        param = {'right': 'detail', 'fr_all_day': 'false', 'room_id': room_id, 'classkind': '8', 'date': date,
                 'act': 'get_rsv_sta', 'fr_start': fr_start, 'fr_end': fr_end}

        res = requests.post(url=fetchUrl, params=param)
        # print(res.text)
        seats = json.loads(res.text).get('data')
        availableSeats = []
        for seat in seats:
            # print(seat)
            if seat.get('freeSta') == 0:
                print(seat.get('title'))
                availableSeats.append(seat)
        print('该时间段内一共' + str(len(availableSeats)) + '个座位可约')

        return availableSeats

    def accurateBooking(self, stuID, passwd, devID, start, end, seatName='登录系统查看'):
        reserveUrl = self.libUrl + "pro/ajax/reserve.aspx"
        cookie = self.login(stuID, passwd)
        if cookie is None:
            msg = stuID + '登录失败，请检查账户配置'
            print(msg)
            self.larkPush.pushText(msg)
            return

        # print("正在为" + stuID + "预定：" + seat.get("title"))
        # param = {"dev_id": str(seat.get("devId")), "lab_id": str(seat.get("labId")), "kind_id": str(seat.get("kindId")),
        #          "type": "dev", "classkind": "8", "start": start, "end": end, "act": "set_resv"}
        param = {"dev_id": devID, "start": start, "end": end, "act": "set_resv"}
        try:
            res = requests.post(url=reserveUrl, params=param, cookies=cookie)
            print(res.text)
            if json.loads(res.text).get('ret') == 1:
                print('预约成功')
                # self.larkPush.pushBookSuccess(stuID, seat.get('title'), start, end)
                self.larkPush.pushBookSuccess(stuID, seatName, start, end)
                # return seat
                return devID
            elif json.loads(res.text).get('msg') == '当前时间预约冲突':
                return 'occupied'
            else:
                msg = stuID + '从' + start + '到' + end + '的预约可能失败，原因为：' + json.loads(res.text).get('msg')
                print(msg)
                self.larkPush.pushText(msg)
                # TODO:添加预约失败处理逻辑
        except TimeoutError:
            msg = stuID + '从' + start + '到' + end + '的预约请求超时'
            print(msg)
            self.larkPush.pushText(msg)
            # TODO:添加超时处理逻辑
        except Exception as e:
            msg = stuID + '从' + start + '到' + end + '的预约出现未知异常：\n' + str(traceback.format_exc())
            print(msg)
            self.larkPush.pushText(msg)
            # TODO:添加异常处理逻辑

    def oneKeyBooking(self, stuID, passwd, date, start, end):
        for room in roomInfo:
            availableSeats = self.fetchAvailableSeatsByRoom(room.get('id'), date, start, end)
            if len(availableSeats) == 0:
                continue
            else:
                devID = self.accurateBooking(stuID, passwd, availableSeats[0].get('devId'), date + ' ' + start,
                                         date + ' ' + end, availableSeats[0].get('title'))
                return devID
