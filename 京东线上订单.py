# -*- coding: utf-8 -*-

#查看京东订单浏览量情况
import pandas as pd

#导入原始数据，清洗假订单
data = pd.read_excel('jingdong/jingdong726.xlsx',sheetname='原始')
data1 = pd.read_excel('xpet/jingdong726.xlsx',sheetname='单日平均浏览')
data = data.dropna()

#转换宠物价格数据类型
data1 = data['宠物价格'].astype(int)
data1 = pd.DataFrame(data1)  
data['宠物价格'] = data1['宠物价格']

#取某几个字段
测试 = data[['下单时间','宠物价格']]

#省份销量排行
data2 = data.groupby(['城市']).size()
data2 = pd.DataFrame(data2)  
data2.columns=['省份销量']
省份销量 = data2.sort(columns='省份销量',ascending=False)

#品种销量排行
data3 = data.groupby(['宠物名称']).size().reset_index()
data3.columns=['宠物名称','宠物销量']
data3 = data3.sort(columns='宠物销量',ascending=False)

#合并销量与PV
df = pd.merge(data1, data3, left_on='宠物名称', right_on='宠物名称')

#总销售额
总销售额 = data.groupby(['是否刷单'])['宠物价格'].sum()
总销售额 = pd.DataFrame(data3)  
总销售额.columns=['真实订单销售额']
总销售额 = 总销售额.sort(columns='真实订单销售额',ascending=False)