# 准备工作
1. 在 [PipeHub](https://www.pipehub.net/#/) 按首页指引，取得 `Callback URL` ，记下最后一段 Token 。
2. 将学号、密码、预约时间、座位号以及上一步取得的 Token 填入脚本内。

其中座位号可在此取得：

![waXPqf.png](https://s1.ax1x.com/2020/09/12/waXPqf.png)
3. 添加 CronTab 任务，如每天6:40执行预约：

`40 6 * * * /home/booking.sh &>/dev/null 2>&1`
