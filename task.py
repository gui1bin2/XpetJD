# -*- coding: utf-8 -*-

#测试
import pandas as pd
import networkx as nx

df = pd.DataFrame([['geneA', 'geneB', 0.05, 'method1'],
                           ['geneA', 'geneC', 0.45, 'method1'],
                           ['geneA', 'geneD', 0.35, 'method1'],
                           ['geneA', 'geneB', 0.45, 'method2']], 
                           columns = ['gene1','gene2','conf','type'])

G= nx.from_pandas_dataframe(df, 'gene1', 'gene2', edge_attr=['conf','type'], 
                                    create_using=nx.Graph())
MG= nx.from_pandas_dataframe(df, 'gene1', 'gene2', edge_attr=['conf','type'], 
                             create_using=nx.MultiGraph())
MG= nx.from_pandas_dataframe(df, 'gene1', 'gene2', edge_attr=['conf','type'], 
                             create_using=nx.MultiGraph())
#修改后
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table('xpet/big.txt',names=['node1','node2','timestamp'],header=None,delim_whitespace=True)
f=pd.DataFrame(df)

G=nx.from_pandas_dataframe(df,'node1','node2',edge_attr=['timestamp'],create_using=nx.MultiGraph())

nx.draw(G,node_size = 50)
N=G.number_of_nodes()
M=G.number_of_edges()

print (N,M)
time=nx.get_edge_attributes(G,'timestamp')

plt.savefig("time.png")
plt.show()
