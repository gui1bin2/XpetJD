# -*- coding: utf-8 -*-

#分析流量变化原因

import pandas as pd

#导入原始数据
data24 = pd.read_excel('jingdong/679204_20170724_全部渠道_商品明细.xls',)
data26 = pd.read_excel('jingdong/679204_20170726_全部渠道_商品明细.xls',)
data24 = data24.dropna()
data26 = data26.dropna()

#提取相关字段
data24 = data24[['商品名称','浏览量']]
data24.columns=['商品名称','24日浏览量']
data26 = data26[['商品名称','浏览量']]
data26.columns=['商品名称','26日浏览量']

#合并
df = pd.merge(data24, data26, left_on='商品名称', right_on='商品名称')

#浏览量做差
df['浏览量变化']=df['24日浏览量']-df['26日浏览量']

#商品名称提取
bands = df['商品名称'].str.slice(3, 7)
df['商品名称'] = bands