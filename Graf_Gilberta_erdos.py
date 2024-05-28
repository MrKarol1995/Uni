import networkx as nx
import random
import matplotlib.pyplot as plt

def erdos_renyi_gilbert_graph(N: int, p: float) -> nx.Graph:
    """
    Generates an Erdős-Rényi Gilbert graph.

    Parameters:
    N (int): Number of nodes.
    p (float): Probability of edge creation.

    Returns:
    nx.Graph: A generated Erdős-Rényi Gilbert graph.
    """
    G = nx.Graph()
    nodes = range(1, N + 1)
    G.add_nodes_from(nodes)

    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if random.random() < p:
                G.add_edge(i, j)
    print(f"Number of edges: {len(G.edges)}")
    return G

def plot_degree_distribution(G: nx.Graph) -> None:
    """
    Plots the degree distribution of the graph.

    Parameters:
    G (nx.Graph): The input graph.
    """
    degrees = [deg for node, deg in G.degree()]
    plt.hist(degrees, bins=range(min(degrees), max(degrees) + 1), density=True)
    plt.title("Degree Distribution")
    plt.xlabel("Degree")
    plt.ylabel("Density")
    plt.show()

def plot_clustering_coefficient_distribution(G: nx.Graph) -> None:
    """
    Plots the clustering coefficient distribution of the graph.

    Parameters:
    G (nx.Graph): The input graph.
    """
    clustering_coefficients = list(nx.clustering(G).values())
    print(f"Clustering coefficients: {clustering_coefficients}")
    plt.hist(clustering_coefficients, bins=20, density=True)
    plt.title("Clustering Coefficient Distribution")
    plt.xlabel("Clustering Coefficient")
    plt.ylabel("Density")
    plt.show()

def draw_graph(G: nx.Graph) -> None:
    """
    Draws the graph.

    Parameters:
    G (nx.Graph): The input graph.
    """
    nx.draw(G, with_labels=True)
    plt.show()

# Example usage
if __name__ == "__main__":
    N = 1000  # Number of nodes
    p = 0.2  # Probability of edge creation
    G = erdos_renyi_gilbert_graph(N, p)
    plot_degree_distribution(G)
    plot_clustering_coefficient_distribution(G)
    #draw_graph(G)
