#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
from lxml import etree
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

if __name__ == '__main__':
     url = 'https://bj.58.com/ershoufang/'
     page_text = requests.get(url=url, headers=headers).text

     # 数据解析
     tree = etree.HTML(page_text)
     # 存储的就是li标签对象
     li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
     fp = open('58.txt', 'w', encoding='utf-8')
     for li in li_list:
         # 局部解析
         title = li.xpath('./div[2]/h2/a/text()')[0]
         print(title)
         fp.write(title + '\n')

