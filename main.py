import csv
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

grafo = nx.Graph()
with open('data_co_autores.csv') as csv_file:
    for row in csv.reader(csv_file, delimiter=','):
        lista_docs = []
        for dos in row:
            lista_docs.append(dos)
        docentes = combinations(lista_docs, 2)

        for docente in docentes:

            if grafo.has_edge(docente[0].upper(), docente[1].upper()):
                grafo[docente[0].upper()][docente[1].upper()]['weight'] = grafo[docente[0].upper()][docente[1].upper()]['weight'] + 1
            else:
                grafo.add_weighted_edges_from([(docente[0].upper(), docente[1].upper(), 1)])


nx.write_gml(grafo, 'data_co_autores_revista.gml')





