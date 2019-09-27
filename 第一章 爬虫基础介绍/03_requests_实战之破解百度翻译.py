#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

import requests
import  json

if __name__ == '__main__':
    # url 指定
    post_url = 'https://fanyi.baidu.com/sug'
    # 进行伪装 UA
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    # post请求参数处理 （桶get请求一至）
    word = input('enter or word:')
    data = {
        'kw': word
    }

    # 请求发送
    response = requests.post(url=post_url,data=data,headers=headers)
    # 获取响应数据 json 方法返回时obj对象 如果确认响应数据json类型 才可以使用json方法对象返回
    dic_obj = response.json()

    # 进行持久化存储
    fileName = word+'.json'
    print(type(fileName))
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('ok')
