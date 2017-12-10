# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:53:36 2017

@author: marko
"""

from pandas import Series, DataFrame
import pandas as pd
import networkx as nx
import sys



""" 
Import Karate club data, create edgelist and djancency matrix
"""

G1 = nx.read_edgelist(r'zachary_karate_club.txt', nodetype=str , create_using=nx.DiGraph(), data=(('weight',float),))

#nx.write_edgelist(G1,'karate_edgelist')
#nx.read_edgelist('karate_edgelist')
nx.write_edgelist(G1,sys.stdout)

karate_matrix=nx.attr_matrix(G,rc_order=G.nodes) 


""" 
Import whom_talks_to_whom data, create edgelist and djancency matrix
"""
# data import and clean (from HW2)
df = pd.ExcelFile(r'HW2_who_talks_to_whom.xlsx')
df = df.parse(df.sheet_names[0]).fillna(0).replace(['-'], [0]).drop('Nodes', 1)

#creates edge list for dfSent(node1, node2, weight)
df = df.stack().reset_index()
df.iloc[:, 0] = df.iloc[:, 0] + 1
df.columns = ['source', 'target','weight']

#remove 0 weights edges
df=df[df.weight != 0]


G2 = nx.from_pandas_dataframe(df, create_using=nx.DiGraph())

#nx.write_edgelist(G2,'class_edgelist')
#nx.read_edgelist('class_edgelist')
nx.write_edgelist(G2,sys.stdout)

class_matrix=nx.attr_matrix(G2,rc_order=G2.nodes) 


"""Begin Girvan Newman here"""
