from exceptions import *
import random


class Node:
    def __init__(self, name, edges):
        self.name, self.edges, self.weight = name, edges, 1
        self.visited = False

    def choose_path(self):
        neighbors = []
        for e in range(len(self.edges)):
            n = self.edges[e].get_way()
            if n:
                neighbors += [e] * int(self.edges[e].pheromone)
        if not neighbors:
            raise EndOfPath
        choice = random.choice(neighbors)
        return self.edges[choice], self.edges[choice].get_way()


class Edge:
    def __init__(self, n1, n2, length):
        self.node1, self.node2 = n1, n2
        self.length = length
        self.min_ph = 10
        self.max_ph = 100
        self.pheromone = self.min_ph
        self.evaporation = 0.95

    def get_way(self):
        if self.node1.visited and self.node2.visited:
            return None
        elif self.node1.visited:
            return self.node2
        else:
            return self.node1

    def put_pheromone(self, amount):
        self.pheromone = min(self.max_ph, self.pheromone + amount)

    def evaporate(self):
        self.pheromone = max(self.min_ph, self.pheromone * self.evaporation)


class Graph:
    def __init__(self, root, nodes, edges):
        self.nodes = []
        for n in nodes:
            self.nodes.append(Node(n, []))
        self.edges = []
        for e in edges:
            n1 = self.find_node(e[0])
            n2 = self.find_node(e[1])
            edg = Edge(n1, n2, e[2])
            self.edges.append(edg)
            n1.edges.append(edg)
            n2.edges.append(edg)
        self.find_node(root).visited = True

    def find_node(self, name):
        for n in self.nodes:
            if n.name == name:
                return n
        return None

    def find_edge(self, n1, n2):
        n = self.find_node(n1)
        for e in n.edges:
            for nn in [e.node1, e.node2]:
                if nn.name == n2:
                    return e
        return None


class Vehicle:
    def __init__(self, capacity, max_range, position, name):
        self.name = name
        self.capacity, self.max_range = capacity, max_range
        self.position = position
        self.path = [position.name]
        self.load, self.fuel = self.capacity, self.max_range
        self.path_ended = False
        self.edge_driven = 0

    def reset(self):
        self.load, self.fuel = self.capacity, self.max_range
        self.position = self.path[0]

    def move(self):
        if self.path_ended:
            return None
        if self.fuel == 0:
            self.path_ended = True
            return None
        if isinstance(self.position, Node):
            try:
                new_p = self.position.choose_path()
                self.position = new_p[0]
                self.edge_driven = 1
            except EndOfPath:
                self.path_ended = True
                return None
        elif isinstance(self.position, Edge):
            if self.edge_driven == self.position.length:
                self.position.put_pheromone(40)
                nn = self.position.get_way()
                if nn and nn.weight <= self.load:
                    self.position = nn
                    self.path.append(nn.name)
                    self.load -= nn.weight
                    nn.visited = True
                else:
                    self.path_ended = True
                    return None
            else:
                self.edge_driven += 1
        self.fuel -= 1


class Colony:
    def __init__(self, v_number, v_capacity, v_range, graph):
        self.vehicles_number, self.vehicle_capacity, self.vehicle_range = v_number, v_capacity, v_range
        self.graph = graph
        self.vehicles = [Vehicle(v_number, v_capacity, graph.nodes[0], str(i + 1)) for i in range(v_number)]

    def iterate(self, num):
        for i in range(num):
            for _ in range(self.vehicle_range):
                self.step()
                finished = True
                for v in self.vehicles:
                    if not v.path_ended:
                        finished = False
                if finished:
                    return None

    def step(self):
        for vehicle in self.vehicles:
            vehicle.move()
        for edge in self.graph.edges:
            edge.evaporate()
