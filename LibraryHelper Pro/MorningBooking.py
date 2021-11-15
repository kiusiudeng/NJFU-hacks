import datetime

import LarkPush
import DateConventer
import LibraryBooking

larkPush = LarkPush.LarkPush()
libraryBooking = LibraryBooking.LibraryBooking()

bookInfo = [
    {
        'name': '你的姓名',
        'stuID': '你的学号',
        'passwd': '你的密码',
        'devID': '固定座位的devId',
        'seatName': '固定座位名称',
        'schedule': {  # 以下是你的计划，请按照格式设置
            '星期一': [
                {'startTime': '8:30', 'endTime': '11:30'},
                {'startTime': '15:30', 'endTime': '17:30'},
                {'startTime': '18:00', 'endTime': '20:30'}
            ],
            '星期二': [
                {'startTime': '9:30', 'endTime': '11:30'},
                {'startTime': '14:00', 'endTime': '16:30'}
            ],
            '星期三': [
                {'startTime': '8:30', 'endTime': '11:30'},
                {'startTime': '14:00', 'endTime': '17:30'},
                {'startTime': '18:00', 'endTime': '20:30'}
            ],
            '星期四': [],
            '星期五': [
                {'startTime': '8:30', 'endTime': '11:30'},
                {'startTime': '14:00', 'endTime': '17:30'},
                {'startTime': '18:00', 'endTime': '20:30'}
            ],
            '星期六': [
                {'startTime': '8:30', 'endTime': '11:30'},
                {'startTime': '18:00', 'endTime': '20:30'}
            ],
            '星期日': []
        }
    },
    # 你可以添加多人的预约信息
]

week_day = DateConventer.get_tomorrow_week_day(datetime.datetime.now())
larkPush.pushText('卷王们早上好！明天是' + week_day + "，即将开始每日例行预约。")
for person in bookInfo:
    msg = person.get('name') + '，我将尝试为你预约明天的：\n'
    for schedule in person.get('schedule').get(week_day):
        msg += schedule.get('startTime') + '~' + schedule.get('endTime') + '\n'
    msg += '预约成功后，请核对预约状态并手动取消不需要的时段。'
    larkPush.pushText(msg)

    # 开始预约
    tomorrow_date = DateConventer.get_tomorrow_date()
    print(tomorrow_date)
    # availableSeats = libraryBooking.fetchAvailableSeatsByRoom("100455356", tomorrow_date, "8:00", "22:00")
    # if len(availableSeats) == 0:
    #     msg = '此时没有空座位了，后续所有预约操作失败。'
    #     larkPush.pushText(msg)
    #     exit()
    # else:
    #     for schedule in person.get('schedule').get(week_day):
    #         libraryBooking.accurateBooking(person.get('stuID'), person.get('passwd'), availableSeats[0],
    #                                        schedule.get('startTime'), schedule.get('endTime'))

    for schedule in person.get('schedule').get(week_day):
        devID = libraryBooking.accurateBooking(person.get('stuID'), person.get('passwd'), person.get('devID'),
                                               tomorrow_date + ' ' + schedule.get('startTime'),
                                               tomorrow_date + ' ' + schedule.get('endTime'), person.get('固定座位'))
        if devID == 'occupied':
            msg = '啊哦，固定座位已经被占了！尝试预约其他座位。'
            larkPush.pushText(msg)
            libraryBooking.oneKeyBooking(person.get('stuID'), person.get('passwd'), tomorrow_date,
                                         schedule.get('startTime'), schedule.get('endTime'))
