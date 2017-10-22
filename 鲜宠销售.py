# -*- coding: utf-8 -*-


import pandas as pd

data = pd.read_excel('xpet/xpet.xlsx',sheetname='线下销售台账')

data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month
data2 = data.groupby(['year','month'])['price'].sum()

#按年月分组销售额
data2 = data.groupby(['year','month'])['price'].sum()
data2 = pd.DataFrame(data2) 
data2.columns=['月销售额']

#按年月分组销售额
data2 = data.groupby(['address'])['price'].sum()
data2 = pd.DataFrame(data2) 
data2.columns=['月销售额']


data2=pd.DataFrame(data2)  


#宠物品种销量降序
data1 = data.groupby(['pet']).size()
data1 = pd.DataFrame(data1)  
data1.columns=['宠物销量']
data1 = data1.sort(columns='宠物销量',ascending=False)