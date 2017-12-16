import random


class Graph


class Node:
    """
    Node in the graph
    """
    def __init__(self, name, edges, weight):
        self.name, self.edges, self.weight = name, edges, weight
        self.visited = False


class Edge:
    """
    Edge in the graph
    """
    def __init__(self, n1, n2, length):
        self.node1, self.node2 = n1, n2
        self.length = length
        self.min_ph = 10
        self.max_ph = 1000
        self.pheromone = self.min_ph
        self.evaporation = 0.97

    def get_way(self, n):
        return self.node1 if self.node2.name == n else self.node2

    def put_pheromone(self, amount):
        self.pheromone = min(self.max_ph, self.pheromone + amount)

#
# class Graph:
#     """
#     The graph itself
#     """
#     def __init__(self, root, nodes, edges):
#         self.nodes = []
#         for n in nodes:
#             self.nodes.append(Node(n, [], 1))   # The weight 1 is fixed in this line
#         self.edges = []
#         for e in edges:
#             n1 = self.find_node(e[0])
#             n2 = self.find_node(e[1])
#             edg = Edge(n1, n2, e[2])
#             self.edges.append(edg)
#             n1.edges.append(edg)
#             n2.edges.append(edg)
#         self.find_node(root).visited = True
#
#     def choose_path(self, node):
#         neighbors = []
#         for e in node.edges:
#             neighbors.append(e.get_way(node.name))
#         ways = []
#         for n in neighbors:
#             if not n.visited:
#                 ways.append(self.find_edge(node.name, n.name))
#         chs = []
#         for i in range(len(ways)):
#             chs += [i] * int(ways[i].pheromone)
#         if not chs:
#             return None
#         else:
#             return random.choice(chs)
#
#     def find_node(self, name):
#         for n in self.nodes:
#             if n.name == name:
#                 return n
#         return None
#
#     def find_edge(self, n1, n2):
#         n = self.find_node(n1)
#         for e in n.edges:
#             for nn in [e.node1, e.node2]:
#                 if nn.name == n2:
#                     return e
#         return None
#
#     def calculate_len(self, path):
#         l = 0
#         for i in range(len(path) - 1):
#             n1, n2 = path[i], path[i+1]
#             l += self.find_edge(n1, n2).length
#         return l
#
#     def evaporate(self):
#         for edge in self.edges:
#             edge.pheromone = max(edge.min_ph, edge.pheromone * edge.evaporation)
#


