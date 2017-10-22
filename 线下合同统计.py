# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:50:24 2017

@author: Administrator
"""

import pandas as pd

#导入原始数据
data11 = pd.read_excel('xpet/线下合同电子归档-已删减版.xlsx',sheetname='1月猫')
data12 = pd.read_excel('xpet/线下合同电子归档-已删减版.xlsx',sheetname='1月狗')
data21 = pd.read_excel('xpet/线下合同电子归档-已删减版.xlsx',sheetname='2月猫')
data22 = pd.read_excel('xpet/线下合同电子归档-已删减版.xlsx',sheetname='2月狗')
data31 = pd.read_excel('xpet/线下合同电子归档-已删减版.xlsx',sheetname='3月猫')
data32 = pd.read_excel('xpet/线下合同电子归档-已删减版.xlsx',sheetname='3月狗')
data41 = pd.read_excel('xpet/线下合同电子归档-已删减版.xlsx',sheetname='4月猫')
data42 = pd.read_excel('xpet/线下合同电子归档-已删减版.xlsx',sheetname='4月狗')
data51 = pd.read_excel('xpet/线下合同电子归档-已删减版.xlsx',sheetname='5月猫')
data52 = pd.read_excel('xpet/线下合同电子归档-已删减版.xlsx',sheetname='5月狗')
data61 = pd.read_excel('xpet/线下合同电子归档-已删减版.xlsx',sheetname='6月猫')
data62 = pd.read_excel('xpet/线下合同电子归档-已删减版.xlsx',sheetname='6月狗')
data71 = pd.read_excel('xpet/线下合同电子归档-已删减版.xlsx',sheetname='7月猫')
data72 = pd.read_excel('xpet/线下合同电子归档-已删减版.xlsx',sheetname='7月狗')
data8 = pd.read_excel('xpet/线下合同电子归档-已删减版.xlsx',sheetname='其他')
data81 = pd.read_excel('xpet/8月截止20号合同.xlsx',sheetname='猫')
data82 = pd.read_excel('xpet/8月截止20号合同.xlsx',sheetname='狗')
data83 = pd.read_excel('xpet/8月截止20号合同.xlsx',sheetname='其他')

data = pd.concat([data11,data12,data21,data22,data31,data32,data41,data42,
                  data51,data52,data61,data62,data71,data72,data8,data81,data82,data83])
data = data[['品种','价格']]
data = data.dropna()

data.to_excel('xpet/合同价格.xlsx',index=False)