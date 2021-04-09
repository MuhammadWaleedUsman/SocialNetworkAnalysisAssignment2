import pandas as pd
import networkx as nx
from matplotlib.pyplot import figure
import collections
import matplotlib.pyplot as plt
df = pd.read_csv('data/CA-AstroPh.txt', sep="\t",
                 header=0)
print(df.head())
dframe = df[['FromNodeId', 'ToNodeId']]
df1 = dframe.head(100)
print(df1)
G = nx.from_pandas_edgelist(dframe, 'FromNodeId', 'ToNodeId', create_using=nx.DiGraph())
# G = nx.erdos_renyi_graph(n=1000, p=1,  seed=None, directed=True)

degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color="b")

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
# ax.set_xticks([d + 0.4 for d in deg])
# ax.set_xticklabels(deg)
#
# # draw graph in inset
# plt.axes([0.4, 0.4, 0.5, 0.5])
# Gcc = G.subgraph(sorted(nx.strongly_connected_components(G), key=len, reverse=True)[0])
# pos = nx.spring_layout(G)
# plt.axis("off")
# nx.draw_networkx_nodes(G, pos, node_size=10)
# nx.draw_networkx_edges(G, pos, alpha=0.4)
plt.show()
