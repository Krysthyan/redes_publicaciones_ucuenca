import networkx as nx
import random

G = nx.Graph()
G.add_edge(1, 2, weight=7)
G.add_edge(1, 3, weight=2)
G.add_edge(1, 4, weight=2)
G.add_edge(1, 5, weight=6)
G.add_edge(2, 3, weight=3)
G.add_edge(4, 5, weight=1)

print(G.has_edge(1,2))
print(G.has_edge(2,10))

# G[1][6]['weight'] = G[1][6]['weight'] + 10
#
# print(G[1][2]['weight'])
