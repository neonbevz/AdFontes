import json
import random


def generate_graph(n_nodes, n_edges, min_len, max_len):
    nodes = ["N" + str(i + 1) for i in range(n_nodes - 1)]
    nodes = ["O"] + nodes
    edges = []
    for j in range(n_edges):
        node = nodes[j % len(nodes)]
        node2 = random.choice(nodes)
        while node2 == node or [node, node2] in edges or [node2, node] in edges:
            node2 = random.choice(nodes)
        edges.append([node, node2])
    for edge in edges:
        edge.append(random.randint(min_len, max_len))
    return "O", nodes, edges


def write_graph(filename, origin, nodes, edges):
    d = {"origin": origin, "nodes": nodes, "edges": edges}
    with open(filename, mode="w") as file:
        file.write(json.dumps(d))


def read_graph(filename):
    with open(filename) as file:
        d = json.loads(file.read())
    return d["origin"], d["nodes"], d["edges"]
