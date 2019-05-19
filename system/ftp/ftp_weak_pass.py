# Author:w8ay
# Name:FTP 弱口令

import HackRequests
from urllib.parse import urlparse
import ftplib


def poc(arg, **kwargs):
    userlist = ["root","admin","www","ftp","anonymous"]
    password = ["123456","admin123","admin","www","ftp"]
    for user in userlist:
        for pwd in password:
            try:
                ftp = ftplib.FTP(arg)
                ftp.login(user,pwd)
                ftp.quit()
                userandpass = (user,pwd)
                return True
            except:
                pass

    result = {
        "name": "FTP若口令",  # 插件名称
        "content": "得到FTP密码",  # 插件返回内容详情，会造成什么后果。
        "url": userandpass,  # 漏洞存在url
        "log": "",
        "tag": "info_leak"  # 漏洞标签
    }
    return False
