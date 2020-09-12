#!/usr/bin/env bash
#********************************************************
# * Author      : Kyouya
# * Email       : kiusiudeng@gmail.com
# * Version     : 1.0
# * Description : 使用crontab定时运行的图书馆自动预约座位脚本。
#********************************************************

# 需要填写的部分，注意图书馆开放时间为7:30~22:00；多个座位号以空格分开
StudentID="YOUR_ID_NUMBER_HERE"
Password="YOUR_PASSWORD_HERE"
StartTime="7:30"
EndTime="22:00"
deskid=(100455441 100455442 100455443 100455444)
PipehubToken="YOUR_PIPEHUB_TOKEN_HERE"
BarkToken="YOUR_BARK_TOKEN_HERE"

# 默认预约日期是明天yyyy-mm-dd
rsvdate=$(date -d next-day +%Y-%m-%d)

# 获取Cookie
curl -s -o /dev/null -c /tmp/cookie.txt http://libic.njfu.edu.cn/ClientWeb/xcus/ic2/Default.aspx

# 登录
function tryLogin() {
    curl -s -b /tmp/cookie.txt -o /tmp/login.txt -d "id=$StudentID&pwd=$Password&act=login" http://libic.njfu.edu.cn/ClientWeb/pro/ajax/login.aspx
    if [ $(awk -F '[,]' '{print $1}' /tmp/login.txt) == "{\"ret\":1" ]; then
        #登录成功
        return 0
    else
        #登录失败
        echo $(awk -F '["]' '{print $10}' /tmp/login.txt) >/tmp/login.txt
        return 1
    fi
}

# 执行预约
function tryReserve() {
    curl -s -b /tmp/cookie.txt -o /tmp/reserve.txt -d "dev_id=$1&type=dev&start=$2+$3&end=$2+$4&act=set_resv" http://libic.njfu.edu.cn/ClientWeb/pro/ajax/reserve.aspx
    if [ $(awk -F '[,]' '{print $1}' /tmp/reserve.txt) == "{\"ret\":1" ]; then
        #预定成功
        return 0
    else
        #预定失败
        echo $(awk -F '["]' '{print $10}' /tmp/reserve.txt) >/tmp/reserve.txt
        return 1
    fi
}

# 消息推送服务
function tryPush() {
    # 企业微信
    curl -s -o /dev/null -d "$1" "https://www.pipehub.net/send/$PipehubToken"

    # Bark for iOS
    # curl -s -o /dev/null "https://api.day.app/$BarkToken/$1/$2$3"
}

# Main
if tryLogin; then
    echo -e "$(date +"%Y-%m-%d %T")：登录成功" >>./log.txt
else
    # 企业微信推送
    tryPush "登录失败，$(cat /tmp/login.txt)"

    # Bark for iOS
    # tryPush "登录失败" "$(cat /tmp/login.txt)"

    exit
fi

for ((i = 0; i < ${#deskid[*]}; i++)); do
    if tryReserve ${deskid[i]} $rsvdate $StartTime $EndTime; then
        curl -s -b /tmp/cookie.txt -o /tmp/result.txt -d "act=get_History_resv&strat=90&StatFlag=New" http://libic.njfu.edu.cn/ClientWeb/pro/ajax/center.aspx
        seat="$(awk -F '[><]' '{print $39}' /tmp/result.txt)"
        time="$(awk -F '[><]' '{print $72}' /tmp/result.txt)~$(awk -F '[ <]' '{print $67}' /tmp/result.txt)"
        rsvid="$(awk -F "['']" '{print $56}' /tmp/result.txt)"
        # 企业微信推送
        tryPush "已预约座位号：$seat
预约时间：$time
预约编号：$rsvid"

        # Bark for iOS
        # tryPush "%E6%88%90%E5%8A%9F%E9%A2%84%E7%BA%A6%E5%BA%A7%E4%BD%8D%EF%BC%9A$seat" "%E9%A2%84%E7%BA%A6%E6%97%B6%E9%97%B4%EF%BC%9A$time%0a" "%E9%A2%84%E7%BA%A6%E7%BC%96%E5%8F%B7%EF%BC%9A$rsvid"

        exit
    fi
done
# 企业微信推送
tryPush "预约失败，无座或您已有预约
$(cat /tmp/reserve.txt)"

#Bark for iOS
# tryPush "预约失败，无座或您已有预约" "$(cat /tmp/reserve.txt)"
