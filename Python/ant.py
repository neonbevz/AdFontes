class Node:
    """
    Node in the transportation graph
    """
    def __init__(self, name, connections_in, connections_out, cost, capacity):
        """
        :param str/int name:
         Name of the node
        :param list(Connection) connections_in:
         List of Connection objects where node2 is this node
        :param list(Connection) connections_out:
         List of Connection objects where node1 is this node
        :param int cost:
         Cost characteristic of the node
        :param int capacity:
         Capacity characteristic of the node
        """
        self.name, self.connections_in, self.connections_out, self.cost, self.capacity = \
            name, connections_in, connections_out, cost, capacity


class Connection:
    """
    Directed ark from node1 to node2
    """
    def __init__(self, node1, node2, cost, capacity, time):
        """
        :param Node node1:
         Start node
        :param Node node2:
         Destination node
        :param int cost:
         Cost characteristic of the ark
        :param int capacity:
         Capacity characteristic of the ark
        :param int time:
         Time characteristic of the ark
        """
        self.node1, self.node2 = node1, node2
        self.cost, self.capacity, self.time = cost, capacity, time


class Solution:
    """
    A phenotype
    """
    def __init__(self, path):
        self.path = path

