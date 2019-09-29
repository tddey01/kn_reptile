#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
import requests
from lxml import etree


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
if __name__ == '__main__':
    # url = 'https://www.aqistudy.cn/historydata/'
    # page_text = requests.get(url=url,headers=headers).text
    # # print(page_text)
    #
    #
    # tree = etree.HTML(page_text)
    # print(tree)
    #
    # host_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    # print(host_li_list)
    #
    # all_city_name = []
    # # 解析到热门城市
    # for li in host_li_list:
    #     host_city_name = li.xpath('./a/text()')[0]
    #     all_city_name.append(host_city_name)
    #
    # # 解析的是全部城市的名称
    # all_li_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # print(all_li_list)
    # for li in all_li_list:
    #     hos_city_name = li.xpath('./a/text()')[0]
    #     all_city_name.append(hos_city_name)
    #     print(hos_city_name)
    # print(all_city_name,len(all_city_name))
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url,headers=headers).text

    tree = etree.HTML(page_text)
    # 解析到热门城市和所有城市对应a标签
    #//div[@class="bottom"]/ul/li/a             # 热门城市a标签的层级关系
    #//div[@class="bottom"]/ul/div[2]/li/a     # 全部城市a标签的层级关系
    all_li_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_name = []
    for  li in all_li_list:
        host_city_name = li.xpath('./text()')[0]
        all_city_name.append(host_city_name)
        print(host_city_name)
    print(all_city_name,len(all_city_name))