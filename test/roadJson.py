# -*- coding: utf-8 -*-
# __author__ = ab
# __time__   = '2021/3/13'
'''
1. 将json文件的数据读取出来
2. 读取key为result  的数据
3. 读取result中rows的数据   [0,1,2,3]
4. 获取rows列表中，有多少条数据
5. 获取rows列表中name=‘张媛媛’ 的flowId
6. 获取rows列表中productName=‘联合贷’ 的条数
7. 获取rows列表中loanAmount>30000 的  flowId
8. rows列表里面flowId依次获取
'''
import json

if __name__ == '__main__':
    '''
    data = 1.读取json
    遍历 data             -- 一筐萝卜，找到130斤的，
    result_data = if(result) 
    计算result_data 的len
    遍历 result_data
    对象 = if ( 包含 name & name = ‘张’ )
    flowId = 对象.flowId
    '''
    with open('../testData/json数据.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    for item_data in data:
        result_data = data['result']['rows']
        print('读取result中rows的数据' + str(result_data))
        print('获取rows列表中，有多少条数据' + str(len(result_data)))
        break

    # with open('../testData/json数据.json', 'r', encoding='utf-8') as file:
    #     json_data = json.load(file)
    #     # 读取json文件
    #     print(json_data)
    #     # 读取key为result  的数据
    #     for key in json_data:
    #         if (key.__eq__('result')):
    #             result_ = json_data[key]
    #             print("读取key为result: " + str(result_))
    #             for rows_ in result_:
    #                 if (result_.__eq__('rows')):
    #                     rows_data = result_['rows']
    #
    #     print('获取rows列表中，有多少条数据: ' + str(len(rows_data)))
    #     for item in rows_data:
    #         if (item.__contains__('name') & item['name'].__eq__('张媛媛')):
    #             print('获取rows列表中name=‘张媛媛’ 的flowId:' + str(item['flowId']))
    #         else:
    #             print('获取rows列表中name !=‘张媛媛’ 的flowId:' + str(item['flowId']))
