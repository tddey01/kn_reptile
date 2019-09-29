#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
# 需求 爬取丑事百科中糗图块下所有的糗图图片
import os, requests, re

if __name__ == '__main__':
    # 创建一个文件夹 保存所有图片
    if not os.path.exists('./qiutuLibs'):
        os.makedirs('./qiutuLibs')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }

    # 设置一个通用的URL模板
    url = 'https://www.qiushibaike.com/pic/%d/'

    for pageNum in range(1,36):

        # 对应页码url地址
        new_url = format(url%pageNum)

        # 使用通用的爬虫对url对应的一整张页面进行爬取
        page_text = requests.get(url=url, headers=headers, verify=False).text  # verify=False 忽略https证书过期 异常错误提示

        # 使用聚焦爬虫将页面中所有数据进行解析/提取
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex, page_text, re.S)
        print(img_src_list)

        for src in img_src_list:
            # 拼接出一个完整的图片地址 url
            src = 'https:' + src
            # 请求到图片的二进制数据
            img_data = requests.get(url=src, headers=headers, verify=False)
            # 生成图片名称
            img_name = src.rsplit('/')[-1]
            # 图片存储的路径
            imgPath = './qiutuLibs' + img_name
            with open(imgPath, 'wb') as fp:
                fp.write(img_data)
                print('图片下载成功>>>> {ok}')
