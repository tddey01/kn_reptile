#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
# UA  User-Agent （请求载体身份标识）
# UA检测 门户网站的服务器会检测对应请求的载体身份标识，如果洁厕到请求载体身份标识为某一个浏览器，
# 说明该请求是一个正常请求，但是如果检测到请求载体身份标识不是基于某一款浏览器的，标识该请求为不正常的请求（爬虫），则服务器端就会很有可能拒绝请求，

# UA伪装 让爬虫对应的请求载体身份标识伪装成某一款浏览器、

import requests

if __name__ == '__main__':
    # UA伪装 将对应的 User-Agent 封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.3'
    }
    url = 'https://www.sogou.com/web'
    # 处理url携带的参数 封装到字典中
    kw = input('enter a word:'),   #是一个元组数据 转成字符串类型kw
    param = {
        'query': kw
    }
    # 对指定的url发起的参数对应的url是携带参数的 。并且请求过程中处理了参数
    response = requests.get(url=url, params=param,headers=headers)

    page_text = response.text
    # print(page_text)
    fileName = str(kw)+'.html'
    print(type(kw))

    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, '保存成功')
