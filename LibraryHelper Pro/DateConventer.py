import datetime
import time


def get_tomorrow_week_day(date):
    tomorrow_day_dict = {
        0: '星期二',
        1: '星期三',
        2: '星期四',
        3: '星期五',
        4: '星期六',
        5: '星期日',
        6: '星期一',
    }
    day = date.weekday()
    return tomorrow_day_dict[day]


def get_tomorrow_date():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)

    return str(tomorrow)
