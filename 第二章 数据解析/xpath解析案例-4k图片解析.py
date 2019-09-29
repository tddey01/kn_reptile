#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
import requests
from lxml import etree
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

if not os.path.exists('./picLibs'):
    os.makedirs('./picLibs')
# url http://pic.netbian.com/4kmeinv/
if __name__ == '__main__':
    # 图片地址
    url =  'http://pic.netbian.com/4kmeinv/'
    response =  requests.get(url=url,headers=headers)

    # 获取页面原始编码格式
    print(response.encoding)
    page_text = response.text

    # print(page_text)
    tree = etree.HTML(page_text)
    # print(tree)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    # print(li_list)
    for li in li_list:
        img_url = 'http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
        print(img_url)
        img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
        # print(img_name)
        # 使用此方法处理中文乱码问题
        img_name = img_name.encode('ISO-8859-1').decode('gbk')
        img_data  = requests.get(url=img_url,headers=headers).content

        print(img_name)
        img_path = './picLibs/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print('图片下载成功....! ! !')