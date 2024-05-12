import random
import networkx as nx
import matplotlib.pyplot as plt


def is_valid(graph, node, color, c):
    '''
    функція перевіряє чи може бути цього кольору ( порівнює з сусідами ) 
    '''
    for neighbor in graph.neighbors(node):  # проходимося по сусідах поточного вузла
        if color[neighbor] == c:  # якщо колір сусіда співпадає з запропонованим кольором
            return False 
    return True


def coloring(graph, node, color, num_colors):
    if node == len(graph):  # якщо всі вузли розфарбовані
        return True
    
    for c in range(num_colors):  # проходимося по кожному кольору
        if is_valid(graph, node, color, c):  # якщо доступний
            color[node] = c  # призначаємо колір
            if coloring(graph, node + 1, color, num_colors):  # рекурсивно розфарбовуємо наступний вузол
                return True
            color[node] = -1  # якщо рішення не знайдено, відкатуємо назад, скидаючи призначений колір
    return False


def run(num_nodes, num_colors, probability):

    n_nodes = num_nodes

    num_colors = num_colors
    colors = [-1] * n_nodes

    G = nx.Graph()
    G.add_nodes_from(range(n_nodes))

    # додаємо ребра між вузлами випадковим чином з ймовірністю probability
    for i in range(n_nodes):
        for j in range(i+1, n_nodes):
            if random.random() < probability:
                G.add_edge(i, j)


    # Перевіряємо, чи існує допустиме рішення розфарбовування, і якщо так, візуалізуємо граф.
    if coloring(G, 0, colors, num_colors):
        color_map = [colors[node] for node in G.nodes()]  # cтворюємо список кольорів для вузлів.
        nx.draw(G, node_color=color_map)  # малюємо граф з розфарбованими вузлами.
        plt.show()  # відображаємо граф.
    else:
        print("Рішення не існує")


run(6, 7 ,0.7)
