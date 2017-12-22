import random


class Node:
    def __init__(self, name, weight, edges):
        self.name, self.weight, self.edges = name, weight, edges

    def choose_path(self):
        choice_list = []
        for ind in range(len(self.edges)):
            choice_list += [ind] * int(self.edges[ind].pheromone)
        return self.edges[random.choice(choice_list)]


class Edge:
    def __init__(self, node1, node2, length):
        self.node1, self.node2, self.length = node1, node2, length
        self.min_ph = 10
        self.max_ph = 100
        self.evaporation = 0.96
        self.pheromone = 10

    def other_node(self, name):
        return self.node2 if self.node1.name == name else self.node1

    def put_pheromone(self, amount):
        self.pheromone = min(self.max_ph, self.pheromone + amount)

    def evaporate(self):
        self.pheromone = max(self.min_ph, self.pheromone * self.evaporation)


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = []
        for n in nodes:
            self.nodes.append(Node(n, 1, []))
        self.edges = []
        for e in edges:
            n1 = self.find_node(e[0])
            n2 = self.find_node(e[1])
            edg = Edge(n1, n2, e[2])
            self.edges.append(edg)
            n1.edges.append(edg)
            n2.edges.append(edg)

    def find_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None

    def find_edge(self, n1, n2):
        n = self.find_node(n1)
        for e in n.edges:
            for nn in [e.node1, e.node2]:
                if nn.name == n2:
                    return e
        return None

    def calculate_len(self, path):
        length = 0
        for i in range(len(path) - 1):
            n1, n2 = path[i], path[i+1]
            length += self.find_edge(n1, n2).length
        return length


class Ant:
    def __init__(self, capacity, max_range, position):
        self.capacity, self.max_range = capacity, max_range
        self.position = position
        self.range_left, self.load = max_range, capacity

    def launch(self):
        edges = []
        path = [self.position.name]
        while self.position.name != "D":
            edge = self.position.choose_path()
            self.range_left -= edge.length
            if self.range_left < 0:
                break
            edges.append(edge)
            other_node = edge.other_node(self.position.name)
            self.load -= other_node.weight
            if self.load < 0:
                break
            path.append(other_node.name)
            self.position = other_node
        path_len = self.max_range - self.range_left
        path_weight = self.capacity - self.load
        return path, path_len, path_weight, edges

    def reset(self, position):
        self.position = position
        self.range_left, self.load = self.max_range, self.capacity


class TwoPointColony:
    def __init__(self, ant_capacity, ant_range, graph):
        self.graph = graph
        self.ant = Ant(ant_capacity, ant_range, graph.find_node("O"))

    def iterate(self, iterations):
        for _ in range(iterations):
            path, path_len, path_weight, path_edges = self.ant.launch()
            self.ant.reset(self.graph.find_node("O"))
            target_reached = True if path[-1] == "D" else False
            fitness = self.distance_fitness(path_len, target_reached)
            self.pheromone(fitness * 5, path_edges)

    def pheromone(self, amount, path_edges):
        for edge in self.graph.edges:
            edge.evaporate()
        for edge in path_edges:
            edge.put_pheromone(amount)

    @staticmethod
    def distance_fitness(distance, target_reached, penalty=0, multiplier=100):
        return multiplier/distance if target_reached else penalty*multiplier/distance
