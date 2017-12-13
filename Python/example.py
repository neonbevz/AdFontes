from ant2 import *

# g = Graph({"O": (("N1", 3), ("N2", 4), ("N3", 3)), "N1": (("N2", 2), ), "N2": (("N3", 1), ("N4", 2)), "N3": ()})
g = Graph("O", ("O", "N1", "N2", "N3", "N4", "N5", "N6", "N7"), (("O", "N1", 3), ("O", "N2", 4), ("O", "N3", 3),
                                                                 ("N1", "N2", 2), ("N2", "N3", 1), ("N2", "N4", 2),
                                                                 ("N3", "N5", 5), ("N2", "N3", 1), ("N4", "N5", 1),
                                                                 ("N4", "N6", 6), ("N5", "N7", 3), ("N6", "N7", 2)))

clny = Colony(5, 15, 15, g)
clny.iterate(10)
for edge in clny.graph.edges:
    print("Edge " + edge.node1.name + "-" + edge.node2.name + ": " + str(edge.pheromone))
