# -*- coding: utf-8 -*-

import pandas as pd

#导入原始数据
data = pd.read_excel('jingdong/7月竞品销售.xlsx')

data1 = data[['日期','心宠','心宠价格']]
data1 = data1.dropna()
data1[data1.心宠 == '蓝猫']
data1[data1.心宠 == '哈士奇']

data2 = data[['日期','狗时代','狗时代价格']]
data2 = data2.dropna()
data2[data2.狗时代 == '金毛']

'''
58心宠狗时代合并统计7月1日-7月27日
'''
data3 = data1[['心宠','心宠价格']]
data3.columns=['宠物','均价']
data4 = data2[['狗时代','狗时代价格']]
data4.columns=['宠物','均价']
data5 = pd.concat([data3, data4])


data3 = pd.DataFrame(data5.groupby(['宠物'])['均价'].size().reset_index())
data4 = pd.DataFrame(data5.groupby(['宠物'])['均价'].mean().reset_index())
data3.columns=['宠物','数量']
data4.columns=['宠物','均价']
df3 = pd.merge(data3, data4, left_on='宠物', right_on='宠物')
df33= pd.DataFrame(df3['均价'].astype(int)) 
df3['均价'] = df33['均价']
df3 = df3.sort(columns='数量',ascending=False)

#数据类型转换
data11 = pd.DataFrame(data1['心宠价格'].astype(int))  
data1['心宠价格'] = data11['心宠价格']

data22 = pd.DataFrame(data2['狗时代价格'].astype(int))  
data2['狗时代价格'] = data22['狗时代价格']

#筛选分组
#58心宠
data3 = pd.DataFrame(data1.groupby(['心宠'])['心宠价格'].size().reset_index())
data4 = pd.DataFrame(data1.groupby(['心宠'])['心宠价格'].mean().reset_index())
data3.columns=['心宠','数量']
data4.columns=['心宠','均价']
df1 = pd.merge(data3, data4, left_on='心宠', right_on='心宠')
df11= pd.DataFrame(df1['均价'].astype(int)) 
df1['均价'] = df11['均价']
df1 = df1.sort(columns='数量',ascending=False)

#狗时代
data5 = pd.DataFrame(data2.groupby(['狗时代'])['狗时代价格'].size().reset_index())
data6 = pd.DataFrame(data2.groupby(['狗时代'])['狗时代价格'].mean().reset_index())
data5.columns=['狗时代','数量']
data6.columns=['狗时代','均价']
df2 = pd.merge(data5, data6, left_on='狗时代', right_on='狗时代')
df22= pd.DataFrame(df2['均价'].astype(int)) 
df2['均价'] = df22['均价']
df2 = df2.sort(columns='数量',ascending=False)