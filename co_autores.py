import csv
import networkx as nx
from itertools import combinations

dict_fn = {}
grafo = nx.Graph()
with open('data_co_autores.csv') as csv_file:
    for row in csv.reader(csv_file, delimiter=','):
        revista = row[len(row) - 1]
        del row[len(row) - 1]
        if revista in dict_fn:
            autores = set(row).union(dict_fn[revista])
        else:
            autores = set(row)
        dict_fn[revista] = autores
for revista in dict_fn:
    comb = combinations(dict_fn[revista], 2)
    for comb_tem in comb:
        if grafo.has_edge(comb_tem[0], comb_tem[1]):
            grafo[comb_tem[0]][comb_tem[1]]['weight'] = grafo[comb_tem[0]][comb_tem[1]]['weight'] + 1
        else:
            grafo.add_weighted_edges_from([(comb_tem[0], comb_tem[1], 1)])

nx.write_gml(grafo, 'data_co_autores.gml')





