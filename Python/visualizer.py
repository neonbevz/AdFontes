import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def visualize(graph):
    froms = [edge.node1.name for edge in graph.edges]
    tos = [edge.node2.name for edge in graph.edges]
    values = [edge.pheromone for edge in graph.edges]
    df = pd.DataFrame({"from": froms, "to": tos, "value": values})
    G = nx.from_pandas_dataframe(df, 'to', 'from', 'value', create_using=nx.Graph())
    edges, colors = zip(*nx.get_edge_attributes(G, 'value').items())
    nx.draw(G, edgelist=edges, edge_color=colors, width=10, edge_cmap=plt.cm.Blues, vmin=0.0, vmax=max(df['value']),
            with_labels=True, node_color='skyblue', node_size=1500)
    plt.show()
#
# df = pd.DataFrame({"from": ["O", "O", "O", "O", "N1", "N1", "N2", "N2", "N3", "N3", "N3", "N4", "N5", "N5", "N6",
#                             "N6", "N6", "N7", "N7", "N8", "N8", "N8", "N9", "N10", "N11", "N12"],
#                    "to": ["N1", "N2", "N3", "N4", "N5", "N6", "N6", "N3", "N8", "N7", "N4", "N7", "N9", "N6", "N9",
#                           "N11", "N8", "N8", "N10", "N11", "N12", "N10", "D", "N12", "D", "D"],
#                    "value": [18, 94, 18, 10, 10, 15, 66, 10, 10, 14, 10, 10, 10, 10, 12, 56, 10, 10, 10, 10, 37, 11,
#                              10, 10, 50, 36]
#                    })

# G = nx.from_pandas_dataframe(df, 'to', 'from', 'value', create_using=nx.Graph())
#
# edges, colors = zip(*nx.get_edge_attributes(G, 'value').items())
# print(edges)
# nx.draw(G, edgelist=edges, edge_color=colors, width=10, edge_cmap=plt.cm.Blues, vmin=0.0, vmax=max(df['value']),
#         with_labels=True, node_color='skyblue', node_size=1500)
#
# plt.show()
