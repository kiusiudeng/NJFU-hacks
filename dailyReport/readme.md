# Daily Report
自动上报每日健康情况。



## 免责声明
此项目仅供相关技术学习研究与交流。由使用本项目产生的任何后果（包括但不限于被学校领导**~~爆破~~**、因学校的~~土豆~~服务器接口不稳定等原因造成打卡失败等）与本项目贡献者无关。



## Quick Start
```
git clone https://github.com/kiusiudeng/NJFU-hacks.git

cd dailyReport

pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```
使用你喜欢的方式编辑 `main.py` ，输入 [uia系统](https://uia.njfu.edu.cn/authserver/login) 的账号密码。
如果你愿意使用 `Server 酱` 进行消息推送，可以 [在此申请](http://sc.ftqq.com/?c=code) `sckey`并填入。留空禁用消息推送功能。
```
python3 main.py
```


## Linux Crontab 自动打卡

```
crontab -e
```
按如下格式新增一行：
```
0 12 * * * /usr/bin/python3 /home/NJFU-hacks/dailyReport/main.py > /dev/null 2>&1
```
其中，`0 12 * * *` 表示将在每天 12：00 执行一次打卡任务。



## 许可证

This project is a part of [NJFU-hacks](https://github.com/kiusiudeng/NJFU-hacks) ,and it is GPL-3.0 Licensed.