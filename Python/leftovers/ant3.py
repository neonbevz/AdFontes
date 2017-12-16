from Python.leftovers.graph import *


class Vehicle:
    """
    "ant" to move around on the graph
    """

    def __init__(self, capacity, max_range, position, name):
        self.name = name
        self.capacity, self.max_range = capacity, max_range
        self.position = position
        self.path = [position.name]
        self.load, self.fuel = self.capacity, self.max_range
        self.path_ended = False
        self.edge_driven = 0

    def reset(self, position):
        self.load, self.fuel = self.capacity, self.max_range
        self.position = position
        self.edge_driven = 0
        self.path = [self.path[0]]
        self.path_ended = False

    def move(self):
        if self.path_ended:
            return None
        elif self.fuel == 0:
            self.path_ended = True
            return None
        elif isinstance(self.position, Node):
            e = self.position.choose_path




