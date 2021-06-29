# -*- coding: utf-8 -*-
# __author__ = ab
# __time__   = '2021/2/21'
# 应用:生产sql语句，旧数据全表备份,而后删除就数据
# 使用:先安装pymysql依赖库,有运行.py文件
'''
cd C:\Users\ASUS\Desktop
pip install mymysql
python copydata.py

'''

import pymysql
import datetime


# 查询所有表名
# todo:根据需求修改数据库参数
def show_table():
    # 链接数据库
    connect = pymysql.connect(host='127.0.0.1', port=3306, database='xs_plm', user='root', password='1234')
    cursor = connect.cursor()
    # 查询所有表名
    show_table = "show tables"
    cursor.execute(show_table)
    fetchall = cursor.fetchall()
    # 关闭链接
    cursor.close()
    connect.close()
    print("数据库表个数= {}".format(len(fetchall)))
    return fetchall


def copy_data(unchange_tablename):
    all_table_name = show_table()
    # 筛选出需要执行的表
    table_names = []
    filter = '_copy'
    if all_table_name:
        for item in all_table_name:
            item = item[0]
            if ((filter in item) is False) and ((item in unchange_tablename) is False):
                table_names.append(item)
    if (all_table_name is False) or (table_names is False):
        print('没有需要执行的表')
        return
    # 拼接sql语句
    print('需要执行的表个数= {}', len(table_names))
    template = 'create table {table_name}_copy{date}0 like {table_name};\n' \
               'insert into {table_name}_copy{date}0 (select * from {table_name});\n' \
               'DELETE from {table_name};\n\n'
    sql = ''
    for table_name in table_names:
        sql = sql + template.format(table_name=table_name, date=str(datetime.date.today()).replace('-', ''))
    return sql


if __name__ == '__main__':
    # 数据保持不变的表,不需要备份,也就不存在删除旧数据
    unchange_tablename = ['channel', 'channel_organization', 'loan_product', 'personnel', 'personnel_agent', 'product',
                          'trust_channel']
    sql = copy_data(unchange_tablename)
    print(sql)
    # 生成sql脚本
    open('.\\copy.sql', 'w').write(sql)  # 自带文件关闭功能，不需要再写f.close()
