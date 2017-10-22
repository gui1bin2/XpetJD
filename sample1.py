# -*- coding: utf-8 -*-
"""
Created on Sun Jul 03 10:34:08 2016

@author: QiYue
"""
#########################导入库函数####################
import random
import copy
import networkx as nx
import pandas as pd
####################随机抽样########################
def random_sample(G,size):
    '''
    G:network
    size:length of nodes for choice
    '''
    samples=random.sample(G,size)
    return samples
###################AUC########################
def AUC(real_edges,false_edges):
    AUC_result=0.0
    for i in range(len(real_edges)):
        if real_edges[i]>false_edges[i]:
            AUC_result=AUC_result+1
        elif real_edges[i]==false_edges[i]:
            AUC_result=AUC_result+0.5            
    return AUC_result/len(real_edges)
############################################
def CN(G,nodeij):
    node_i=nodeij[0]#节点1
    node_j=nodeij[1]#节点2 
    neigh_i=set(G.neighbors(node_i))#节点1的邻居节点
    neigh_j=set(G.neighbors(node_j))#节点2的邻居节点
    neigh_ij=neigh_i.intersection(neigh_j)#两节点的共同邻居节点
    num_cn=len(neigh_ij)     #长度=数量  
    return num_cn         
##############################
def PRECISION(real_edges,false_edges,L):
    topL=[]
    cn_real=sorted(real_edges, key=lambda x:x[1],reverse=True)#按CN值排序
    cn_false=sorted(false_edges, key=lambda x:x[1],reverse=True)
    i=0
    j=0
    while len(topL)<=L:
        if cn_real[i][1]>cn_false[j][1]:
            topL.append(cn_real[i])
            i=i+1
        elif cn_real[i][1]< cn_false[j][1]:
            topL.append(cn_false[j])
            j=j+1
        else:
            same=[cn_real[i], cn_false[j]]
            a=random.choice(same)
            topL.append(a)
            same.remove(a)
            topL.append(same)
            i=i+1
            j=j+1     
    m=0.0
    for i in range(L):
        if topL[i] in cn_real[0:L-1]:
            m=m+1           
    return m/L   
################################################
#G=nx.read_edgelist(df)  #读取网络
#G=nx.read_weighted_edgelist('newdata.txt')
filename = 'userID_userID_time.txt'
df = pd.read_csv(filename,names=['node1','node2','timestamp'],header=None,delim_whitespace=True)
f=pd.DataFrame(df)

G=nx.from_pandas_dataframe(df,'node1','node2',edge_attr='timestamp',create_using=nx.MultiGraph())

N =G.number_of_nodes()  #节点数量
print N
f =0.95
 #抽样节点比例，可改，但要保证包含足够多的待抽样连边
Sample=random_sample(G,int(N*f))  #抽样，得到抽样节点列表

length=int(0.1*len(G.edges())) #抽样连边比例，10%
i=10  #从第10个节点开始搜索，可改
b=0   #抽样网络连边数量
while b<length:
    sample_graph=nx.subgraph(G, Sample[:i])#前i个节点组成的抽样网络
    b=sample_graph.number_of_edges() #抽样网络包含的连边数量
    i+=1   #节点数量加1，继续搜索
print 'end in %dth node '%i  #知道i的值，方便下一次调整i的大小，降低运行时间

#################################test_list and no_list#########
train_G = copy.deepcopy(G)#复制网络
test_list=sample_graph.edges()#测试集
for i in range(len(test_list)):
    train_G.remove_edge(test_list[i][0],test_list[i][1])#移除测试集中的连边，剩余90%做训练集
    
no_list=[]                           #要预测的  
while len(no_list)<len(test_list):
    index_1=random.choice(G.nodes())#随机选择一个节点
    index_2=random.choice(G.nodes())#随机选择一个节点
    try:
        G[index_1][index_2]>0     #如果两节点间存在连边，继续；否则执行except        
    except:
        if index_1!=index_2:
            no_list.append((min(index_1,index_2),max(index_1,index_2))) #连边（node1，node2）
####################################################
CN_real=[]
CN_false=[]
for linkij in test_list:
    CN_real.append(CN(train_G,linkij))#计算CN
for linkij in no_list:
    CN_false.append(CN(train_G,linkij))#计算CN
print 'AUC = ',AUC(CN_real,CN_false)#计算AUC
###############
CN_real=[]
CN_false=[]
for linkij in test_list:
    CN_real.append((linkij,CN(train_G,linkij)))#计算CN
for linkij in no_list:
    CN_false.append((linkij,CN(train_G,linkij)))#计算CN
#########################
L=100  #可以更改，但要保证其值小于测试集长度
print 'precision = ',PRECISION(CN_real,CN_false,L)#计算precision