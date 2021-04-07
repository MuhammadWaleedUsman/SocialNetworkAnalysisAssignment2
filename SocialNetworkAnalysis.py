import pandas as pd
import networkx as nx
from matplotlib.pyplot import figure

df = pd.read_csv('data/CA-GrQc.txt', sep="\t",
                 header=0)
print(df.head())
dframe = df[['FromNodeId', 'ToNodeId']]
df1 = dframe.tail(50)

G = nx.from_pandas_edgelist(dframe, 'FromNodeId', 'ToNodeId',
                            create_using=nx.DiGraph())
if nx.is_connected:
    print('Connected')
else:
    print('Not Connected')

# print(G['methazolamide'])

if nx.is_strongly_connected:
    print("yes")

# for key in G:
#     print('Connections of ' + key + ' = ' + str(len(G[key])))

a = figure(figsize=(10, 8))
nx.draw_shell(G, with_labels=True)
a.show()
