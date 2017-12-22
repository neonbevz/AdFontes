from two_point_ant import *
from graph_data import *
from visualizer import *

origin, nodes, edges = read_graph("OD-12-graph.json")

g = Graph(nodes, edges)

clny = TwoPointColony(7, 20, g)

clny.iterate(10000)
for edge in clny.graph.edges:
    print("Edge: " + edge.node1.name + "-" + edge.node2.name + "\nPheromone: " + str(edge.pheromone))
visualize(clny.graph)
