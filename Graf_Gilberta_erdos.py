import networkx as nx
import random
import matplotlib.pyplot as plt
import scipy

def erdos_renyi_gilbert_graph(N, p):
    G = nx.Graph()
    nodes = range(1, N+1)
    G.add_nodes_from(nodes)

    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if random.random() < p:
                G.add_edge(i, j)
    print(len(G.edges))
    return G

def plot_degree_distribution(G):
    degrees = [deg for node, deg in G.degree()]
    plt.hist(degrees, bins=range(min(degrees), max(degrees)+1), density=True)
    plt.title("Degree Distribution")
    plt.xlabel("Degree")
    plt.ylabel("Density")
    plt.show()

def plot_degree_distribution(G):
    degrees = [deg for node, deg in G.degree()]
    plt.hist(degrees, bins=range(min(degrees), max(degrees)+1), density=True)
    plt.title("Degree Distribution")
    plt.xlabel("Degree")
    plt.ylabel("Density")
    plt.show()

def plot_clustering_coefficient_distribution(G):
    clustering_coefficients = list(nx.clustering(G).values())
    print(clustering_coefficients)
    plt.hist(clustering_coefficients, bins=20, density=True)
    plt.title("Rozkład`")
    plt.xlabel("współczynniki")
    plt.ylabel("gestosc")
    plt.show()

def plot_shortest_path_distribution(G):
    shortest_paths = nx.shortest_path_length(G)
    all_shortest_paths = []
    for node1, paths in shortest_paths:
        for node2, length in paths.items():
            all_shortest_paths.append(length)
    plt.hist(all_shortest_paths, bins=range(0, max(all_shortest_paths)+1), density=True)
    plt.title("Shortest Path Distribution")
    plt.xlabel("Shortest Path Length")
    plt.ylabel("Density")
    plt.show()

def draw_graph(G):
    nx.draw(G, with_labels=True)
    plt.show()

# Przykładowe użycie
N = 1000  # Liczba wierzchołków
p = 0.4  # Prawdopodobieństwo połączenia wierzchołków
G = erdos_renyi_gilbert_graph(N, p)
plot_degree_distribution(G)
plot_clustering_coefficient_distribution(G)
# plot_shortest_path_distribution(G)

#draw_graph(G)