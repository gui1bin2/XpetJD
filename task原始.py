# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 16:38:32 2017

@author: ThinkPad
"""
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

filename = 'newdata.txt'
df = pd.read_csv(filename,names=['node1','node2','timestamp'],header=None,delim_whitespace=True)
f=pd.DataFrame(df)

G=nx.from_pandas_dataframe(df,'node1','node2',edge_attr='timestamp',create_using=nx.MultiGraph())
nx.draw(G,node_size = 50)
N=G.number_of_nodes()
M=G.number_of_edges()

print N,M
time=nx.get_edge_attributes(G,'timestamp')



plt.savefig("time.png")
plt.show()
