import random
import itertools
import networkx as nx
import matplotlib.pyplot as plt

def is_valid(graph, node, color, c):
    for neighbor in graph.neighbors(node):
        if color[neighbor] == c:
            return False
    return True

def coloring(graph, node, color, num_colors):
    if node == len(graph):
        return True
    
    for c in range(num_colors):
        if is_valid(graph, node, color, c):
            color[node] = c
            if coloring(graph, node + 1, color, num_colors):
                return True
            color[node] = -1
    return False

n_nodes = 15

G = nx.Graph()
G.add_nodes_from(range(n_nodes))

for i in range(n_nodes):
    for j in range(i+1, n_nodes):
        if random.random() < 0.3:
            G.add_edge(i, j)

num_colors = 4
colors = [-1] * n_nodes

if coloring(G, 0, colors, num_colors):
    color_map = [colors[node] for node in G.nodes()]
    nx.draw(G, node_color=color_map)
    plt.show()
else:
    print("No solution exists")