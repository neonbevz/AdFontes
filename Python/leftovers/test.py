from Python.old_ant import *

g = Graph("O", ["O", "N1", "N2", "N3"], [["O", "N1", 3], ["O", "N2", 3], ["O", "N3", 3]])
n = g.find_node("O")
results = []
for i in range(1000):
    results.append(n.choose_path()[1].name)
print(results.count("N1"))
print(results.count("N2"))
print(results.count("N3"))
print("\n")
e = n.edges[0]
e.put_pheromone(50)
results = []
for i in range(1000):
    results.append(n.choose_path()[1].name)
print(results.count("N1"))
print(results.count("N2"))
print(results.count("N3"))