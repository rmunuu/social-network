import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

n = 50
p = 0.12

np.random.seed(42)

G = nx.gnp_random_graph(n, p)
pos = nx.spring_layout(G)
color_map = np.random.choice(['blue', 'red'], size=50)
options = {
    'node_color':color_map,
    'pos':pos,
    'node_size':40,
    'width':0.1
}
nx.draw(G, **options)
plt.savefig('2.png')
plt.clf()
nx.draw(G, **options)
plt.savefig('3.png')