#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
import requests, json

if __name__ == '__main__':
    url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    id_list = []  # 存放企业id
    all_data_list = [] # 存放所有企业的详情数据
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }

    for  page in range(1,6):
        page = str(page)
        data = {
            'on': 'true',
            'page':page,
            'pageSize': '15',
            'productName': '',
            'conditionType': ' 1',
            'applyname': '',
            'applysn': '',
        }

        json_list = requests.post(url=url, data=data, headers=headers).json()

        for dic in json_list['list']:
            id_list.append(dic['ID'])
    print(id_list)

    # 获取企业详情数据
    post_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id': id
        }
        datai_json = requests.post(url=post_url,headers=headers,data=data).json()
        print(datai_json)
        all_data_list.append(datai_json)
    fp = open('./allData.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    print('over!!!')