from old_ant import *
from graph_data import *


# g = Graph("O", ("O", "N1", "N2", "N3", "N4", "N5", "N6", "N7"), (("O", "N1", 3), ("O", "N2", 4), ("O", "N3", 3),
#                                                                  ("N1", "N2", 2), ("N2", "N3", 1), ("N2", "N4", 2),
#                                                                  ("N3", "N5", 5), ("N2", "N3", 1), ("N4", "N5", 1),
#                                                                  ("N4", "N6", 6), ("N5", "N7", 3), ("N6", "N7", 2)))

origin, nodes, edges = generate_graph(100, 2000, 3, 10)
write_graph("100-graph.json", origin, nodes, edges)
# origin, nodes, edges = read_graph("100-graph.json")

g = Graph(origin, nodes, edges)

clny = Colony(10, 60, 600, g)
clny.iterate(1)

for vehicle in clny.vehicles:
    print(vehicle.path)
    print(g.calculate_len(vehicle.path))
print("\n")

clny.iterate(10)

for vehicle in clny.vehicles:
    print(vehicle.path)
    print(g.calculate_len(vehicle.path))

o = clny.graph.find_node("O")
for e in o.edges:
    print(e.node1.name, e.node2.name, e.pheromone)
for _ in range(5):
    print(o.choose_path()[1].name)

clny.iterate(100000)

print("\n")
for vehicle in clny.vehicles:
    print(vehicle.path)
    print(g.calculate_len(vehicle.path))

o = clny.graph.find_node("O")
for e in o.edges:
    print(e.node1.name, e.node2.name, e.pheromone)
for _ in range(5):
    print(o.choose_path()[1].name)
