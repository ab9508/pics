# -*- coding: utf-8 -*-
# __author__ = ab
# __time__   = '2021/2/16'

import sqlite3
import urllib


# 数据落库，暂时没有去重
def insert(items):
    if items:
        print('准备落库,len= {}'.format(len(items)))
        for item in items:
            connect = sqlite3.connect('pics.db')
            cursor = connect.cursor()
            insert = '''
                INSERT INTO pics (title,url,height,width,type,author,keyword)
                values (?,?,?,?,?,?,?)
            '''
            keyword = item['imgDefaultUrl']
            keyword = urllib.parse.unquote(keyword[keyword.index('query') + 6: keyword.index('&forbidqc')])
            param = (
                item['title'], item['picUrl'], item['height'], item['width'], item['type'], item['author'],
                keyword)
            cursor.execute(insert, param)
            connect.commit()
        cursor.close()
        connect.close()
        print("落库成功")
    else:
        print("数据为空")
    pass


def save_data(items):
    # 建表
    create_table()
    # 数据落库
    insert(items)
    pass


def create_table():
    print('准备建表')
    connect = sqlite3.connect('pics.db')
    cursor = connect.cursor()
    create_table = '''
    CREATE TABLE if not exists  pics(
	    id integer primary key autoincrement ,-- '主键',
	    title text ,-- '主题',
	    url text ,-- '链接',
	    height int ,-- '高',
	    width text ,-- '宽',
	    type tinyint ,-- '类型',
	    author varchar, -- '来源'
	    keyword varchar -- '关键字'
        ); -- 图片表
    '''
    cursor.execute(create_table)
    connect.commit()
    cursor.close()
    connect.close()
    print("建表成功")


# 根据keyword查询数据
def select_keyword(keyword):
    print('准备查询数据,keyword= {}'.format(keyword))
    connect = sqlite3.connect('pics.db')
    cursor = connect.cursor()
    select_keyword = '''
    SELECT url from pics where keyword like ?
    '''
    if keyword == '':
        keyword = ''
    cursor.execute(select_keyword, ('%' + keyword + '%',))
    print(select_keyword)
    fetchall = cursor.fetchall()
    cursor.close()
    connect.close()
    print("查询成功")
    return fetchall


if __name__ == '__main__':
    select_keyword('美女')

    # print(str[index, str_index])
