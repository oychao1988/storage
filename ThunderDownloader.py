import os
import time

"""
启动迅雷下载电影
1. 选项设置
    1.1 直接建立任务
    1.2 启动迅雷后自动开启未完成任务
2. 流程思路
    2.1 打开迅雷待机
    2.2 从云端获取链接添加到下载列表下载
    2.3 检查下载状况，避免重复下载

"""

urls = ["ftp://ygdy8:ygdy8@yg45.dydytt.net:8329/阳光电影www.ygdy8.com.镰仓物语.BD.720p.国日双语中字.mkv",
           "ftp://ygdy8:ygdy8@yg45.dydytt.net:3148/阳光电影www.ygdy8.com.反贪风暴3.HD.1080p.国语中字.mp4",
            ]

for url in urls:
    cmd = r'"D:\Program Files (x86)\Thunder Network\Thunder\Program\Thunder.exe" {url}'.format(url=url)
    result = os.system(cmd)
    print('lalala')
    time.sleep(10)
