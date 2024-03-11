import networkx as nx
import numpy as np
from matplotlib import pyplot as plt


def task2():
    _, axes = plt.subplots()
    axes.plot([0, 1, 2, 3, 4, 5, 6], [0, 2, 4, 6, 4, 2, 0])
    plt.show()


def task3():
    G = nx.Graph()
    G.add_edge('A', 'B')
    G.add_edge('B', 'D')
    G.add_edge('A', 'C')
    G.add_edge('C', 'D')
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    plt.show()


def task4():
    # nazwy wierzchołków
    VV = [1, 2, 3, 4, 5]

    # lista krawędzi
    WW = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (3, 5)]

    # słownik, pozycje wierzchołków
    Vx = {1: -5, 2: 1, 3: 2, 4: 3, 5: 4}
    Vy = {1: 0, 2: 1, 3: 0, 4: -1, 5: 0}

    g = nx.Graph()

    # pusty słownik
    gpos = {}

    # wypełnienie słownika wierzchołkami
    # pętla for przechodzi przez wszystkie elementy 'VV'
    for v in VV:
        g.add_node(v)
        gpos[v] = [Vx[v], Vy[v]]

    # zagnieżdżone pętle for
    for v1 in VV:
        for v2 in VV:
            # sprawdzenie czy krawędź istnieje w 'WW'
            if (v1, v2) in WW:
                # jeśli istnieje, to ustaw etykietę na odległość euklidesową
                # funkcja 'str' zwraca ciąg znaków
                # funkcja 'np.sqrt' zwraca pierwiastek
                # symbol '**' oznacza potęgowanie
                label = str(np.sqrt((Vx[v1] - Vx[v2]) ** 2 + (Vy[v1] - Vy[v2]) ** 2))
                # dodaj wagi do krawędzi
                g.add_weighted_edges_from([(v1, v2, label)])

    # wyświetl żółte wierzchołki z etykietami w ustalonych wcześniej pozycjach
    nx.draw(g, gpos, with_labels=True, node_color='yellow')

    # pobierz i wyświetl etykiety
    labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, gpos, edge_labels=labels)

    # wyświetl graf
    plt.show()


def task5():
    x_start = int(input("Enter starting point of the graph: "))
    x_end = int(input("Enter ending point of the graph: "))

    graph_color = input("Enter color of the graph: ")

    functions_to_plot = input("""
    Enter functions to Plot (separated by space). 
    1. y = x
    2. y = sin(x)
    3. y = cos(x)
    4. y = x^3
    """).split()

    x = np.linspace(x_start, x_end, 50)
    _, ax = plt.subplots(figsize=(10, 5))

    for func in functions_to_plot:
        if func == "1":
            ax.plot(x, x, color=graph_color, label='y = x')
        elif func == "2":
            ax.plot(x, np.sin(x), color=graph_color, label='y = sin(x)')
        elif func == "3":
            ax.plot(x, np.cos(x), color=graph_color, label='y = cos(x)')
        elif func == "4":
            ax.plot(x, pow(x, 3), color=graph_color, label='y = x^3')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title("Wykres")
    ax.legend()
    plt.show()


def lab1():
    task2()
    task3()
    task4()
    task5()


if __name__ == "__main__":
    lab1()
