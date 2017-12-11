# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:53:36 2017

@author: marko
"""

import pandas as pd
import networkx as nx
import sys
import matplotlib.pyplot as plt
from networkx.algorithms.community.centrality import girvan_newman
import community



""" 
Import Karate club data, create edgelist and djancency matrix
"""

G1 = nx.read_edgelist(r'zachary_karate_club.txt', nodetype=str , create_using=nx.Graph(), data=(('weight',float),))
#nx.write_edgelist(G1,sys.stdout)
karate_matrix=nx.attr_matrix(G1,rc_order=G1.nodes) 

""" Girvan Newman method """
comp = girvan_newman(G1)
x=tuple(sorted(c) for c in next(comp))

plt.figure(figsize=(13,13))
pos = nx.spring_layout(G1)
nx.draw_networkx_nodes(G1,pos,nodelist=x[1],node_color='green')
nx.draw_networkx_nodes(G1,pos,nodelist=x[0],node_color='red')
nx.draw_networkx_labels(G1,pos,font_size=10,font_family='sans-serif')
nx.draw_networkx_edges(G1,pos)
plt.axis('off')
plt.show()


"""Louvain community """
part = community.best_partition(G1)
values = [part.get(node) for node in G1.nodes()]

plt.figure(figsize=(13,13))
pos=nx.spring_layout(G1)
nx.draw_networkx_nodes(G1,pos,cmap = plt.get_cmap('jet'),node_color = values, )
nx.draw_networkx_labels(G1,pos,font_size=10,font_family='sans-serif')
nx.draw_networkx_edges(G1,pos,alpha=0.5)
plt.axis('off')
plt.show()



""" 
Import whom_talks_to_whom data, create edgelist and djancency matrix
"""
df = pd.ExcelFile(r'HW2_who_talks_to_whom.xlsx')
df = df.parse(df.sheet_names[0]).fillna(0).replace(['-'], [0]).drop('Nodes', 1)
df = df.stack().reset_index()
df.iloc[:, 0] = df.iloc[:, 0] + 1
df.columns = ['source', 'target','weight']
df = df.loc[ (df['weight'] != 0) & (df['source'] != 16) & (df['target'] != 16)]



G2 = nx.from_pandas_dataframe(df, create_using=nx.Graph())
#nx.write_edgelist(G2,sys.stdout)
class_matrix=nx.attr_matrix(G2,rc_order=G2.nodes) 


""" Girvan Newman method """
comp = girvan_newman(G2)
x=tuple(sorted(c) for c in next(comp))

plt.figure(figsize=(13,13))
pos = nx.spring_layout(G2)
nx.draw_networkx_nodes(G2,pos,nodelist=x[1],node_color='green')
nx.draw_networkx_nodes(G2,pos,nodelist=x[0],node_color='red')
nx.draw_networkx_labels(G2,pos,font_size=10,font_family='sans-serif')
nx.draw_networkx_edges(G2,pos)
plt.axis('off')
plt.show()

"""Louvain community """
part = community.best_partition(G2)
values = [part.get(node) for node in G2.nodes()]

plt.figure(figsize=(13,13))
pos=nx.spring_layout(G2)
nx.draw_networkx_nodes(G2,pos,cmap = plt.get_cmap('jet'),node_color = values, )
nx.draw_networkx_labels(G2,pos,font_size=10,font_family='sans-serif')
nx.draw_networkx_edges(G2,pos,alpha=0.5)
plt.axis('off')
plt.show()
