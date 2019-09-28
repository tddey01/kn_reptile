#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 本地一个html文档中的数据加载到该对象中
    fp = open('./test.html', 'r', encoding='utf8')
    soup = BeautifulSoup(fp,'lxml')
    # print(soup.a) # soup.tagName 返回的是html中第一个tagName标签
    # # print(soup.a)
    # print(soup.find('div'))   # 等同于soup.div用发
    # print(soup.find('div',class_='song'))  # 标签属性定位

    # print(soup.select('.tang'))  # 属性定位标签  select（某种选择器（id，class，标签选择器） 返回一个列表
    # print(soup.select('.tang > ul > li > a')[0]) # 层级选择 > 层级选择器 >标识单个层级
    # print(soup.select('.tang > ul > li  a')[0]) #  空格标识多个层级
    # print(soup.select('.tang > ul a')[0].get_text())   # 获取标签之间文文本内容数据
    # print(soup.find('div',class_ = 'song').text)  # 可以获取某一个标签中所有的文本内容
    # print(soup.find('div', class_='song').string)  # 只可以获取该标签下面直系的文本内容

    #  获取标签中属性值：
    print(soup.select('.tang > ul a ')[0]['href'])  # 获取标签中属性值

