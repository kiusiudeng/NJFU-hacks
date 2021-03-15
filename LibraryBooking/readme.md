# 一点说明

## 座位号

![waXPqf.png](https://s1.ax1x.com/2020/09/12/waXPqf.png)

## 添加 CronTab 任务

如每天7:30执行预约：

`30 7 * * * /home/booking.sh &>/dev/null 2>&1`

`30 7 * * * /home/main.py &>/dev/null 2>&1`

## 关于 Python 版

1. 代码注释都写的很清楚了
2. 请提前安装依赖：

`pip3 install arrow`

`pip3 install requests`