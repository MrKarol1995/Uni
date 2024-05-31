import os
import networkx as nx
import random
import matplotlib.pyplot as plt
from PIL import Image


def random_walk_simulation(graph, start_node, num_steps, output_filename, width=800, height=600):
    pos = nx.spring_layout(graph)  # Pozycje wierzchołków na grafie na podstawie algorytmu, Fruchterman-Reingold

    # Inicjalizacja listy odwiedzonych wierzchołków
    visited_nodes = [start_node]

    # Tworzenie kolejnych kroków symulacji
    for step in range(num_steps):
        current_node = visited_nodes[-1]
        next_node = random.choice(list(graph.neighbors(current_node)))
        visited_nodes.append(next_node)

        # Rysowanie grafu tylko raz
        if step == 0:
            plt.figure()

        nx.draw_networkx_nodes(graph, pos=pos, nodelist=visited_nodes, node_color='blue')
        nx.draw_networkx_nodes(graph, pos=pos, nodelist=[current_node, next_node], node_color='red')
        nx.draw_networkx_labels(graph, pos=pos)
        nx.draw_networkx_edges(graph, pos=pos, alpha=0.5)
        plt.title(f'Krok: {step + 1}')

        # Zapisywanie grafu do pliku obrazowego
        plt.savefig(f'graph_step_{step + 1}.png')
        plt.close()  # Zamknięcie bieżącego wykresu

    # Dostosowanie rozmiaru i rozdzielczości obrazów
    images = []
    for step in range(num_steps):
        image = Image.open(f'graph_step_{step + 1}.png')
        image.thumbnail((width, height), Image.LANCZOS)
        images.append(image)

    # Usunięcie wygenerowanych plików PNG
    for filename in os.listdir():
        if filename.startswith("graph_step_") and filename.endswith(".png"):
            os.remove(filename)

    # Zapisanie animacji GIF
    images[0].save(output_filename, save_all=True, append_images=images[1:], duration=500, loop=0)
    print(f"Animacja została zapisana w pliku {output_filename}")


random.seed(42)
random_graph = nx.gnm_random_graph(20, 30)
start_node = random.choice(list(random_graph.nodes))
random_walk_simulation(random_graph, start_node, 10, "random_walk.gif", width=800, height=600)
