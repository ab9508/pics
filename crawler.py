# -*- coding: utf-8 -*-
# __author__ = ab
# __time__   = '2021/2/15'
# 爬取网站数据

import urllib
import json
import picsdb


# 参数说明,param:图片集,num:数量
def save(param, num):
    # 获取源码
    crawler_sogou(param, num)


def crawler_sogou(param, num):
    print("准备爬取搜狗")
    # 获取网站源码
    param = urllib.parse.quote(param)  # 转义
    url = 'https://pic.sogou.com/napi/pc/searchList?mode=1&start=0&xml_len={}&query={}'.format(num, param)
    print("url= {}".format(url))
    # 伪装成浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    try:
        request = urllib.request.Request(url, headers=headers, method='GET')
        response = urllib.request.urlopen(request)
        data = response.read().decode("utf-8")
        # print(type(data))
        # print(data)
        print("准备提取数据")
        # 转化为json
        data_json = json.loads(data)
        # 获取所有图片
        items = data_json['data']['items']
        # print(items)
        # downloads(items)
        # 数据落库
        picsdb.save_data(items)

        print('爬取搜狗完毕')
        return data
    except urllib.error.URLError as e:
        if headers(e, 'code'):
            print(e.code)
        if headers(e, 'reason'):
            print(e.reason)


# 链接下载
def downloads(items):
    picUrl = []
    for item in items:
        picUrl.append(item['picUrl'])
    print('picUrl= {}'.format(picUrl))
    print('len(picUrl)= {}'.format(len(picUrl)))
    # 下载
    print("准备串行下载")
    m = 0
    for url in picUrl:
        print('m= {}, url= {}'.format(str(m), url))
        try:
            urllib.request.urlretrieve(url, "D://downloads//pics//" + str(m) + '.jpg')
            m = m + 1
        except Exception as e:
            print(e)


# 先爬取数据，再获取链接
# 参数说明,keyword：相册集,默认为图片，数量默认100，
def get_url(keyword):

    if keyword == '':
        keyword = '图片'
    save(keyword, 100)
    data_db = picsdb.select_keyword(keyword)
    data = []
    if data_db:
        print('len(data_db)= {}'.format(len(data_db)))
        for item in data_db:
            data.append(item[0])
    return data


if __name__ == '__main__':
    save('图片', 1)
