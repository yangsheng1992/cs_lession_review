#!/usr/bin/python
# -*- coding: utf-8 -*-


import os

if __name__ == '__main__':
    # crawler = Crawler(0.05)  # 抓取延迟为 0.05
    #
    # crawler.start('刘亦菲', 1, 2)  # 抓取关键词为 “美女”，总数为 1 页（即总共 1*60=60 张），开始页码为 2
    # crawler.start('二次元 美女', 10, 1)  # 抓取关键词为 “二次元 美女”，总数为 10 页（即总共 10*60=600 张），起始抓取的页码为 1
    # crawler.start('帅哥', 5)  # 抓取关键词为 “帅哥”，总数为 5 页（即总共 5*60=300 张）
    import requests
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        # 此条少了就会"Forbid spider access"
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
        # 此条少了就会"Forbid spider access"
        'Upgrade-Insecure-Requests': '1'
    }
    # 爬虫主体
    keyword = input("请输入要搜索的图片关键字：")
    current_path = os.path.dirname(__file__)  # 获取当前目录
    os.mkdir(current_path + '\\' + keyword)  # 新建文件夹
    for num in range(0, 3):  # 一次请求返回30张图，此处循环3次，爬取 90 张图片
        url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&z=&ic=0&word=' + keyword + '&face=0&istype=2&nc=1&pn=' + str(
            num * 30) + '&rn=30'
        response = requests.get(url=url, headers=headers).json()
        for index in range(len(response['data']) - 1):
            print(response['data'][index]['thumbURL'])
            print(num * 30 + index)
            # 从拿到的网址里下载图片
            img_data = requests.get(response['data'][index]['thumbURL']).content
            # 存图
            with open(current_path + '\\' + keyword + '\\' + str(num * 30 + index) + '.jpg', 'wb', )as fp:
                fp.write(img_data)
