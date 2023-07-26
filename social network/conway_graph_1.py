import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pprint

n = 100
p1 = 0.12
p2 = 0.8 # red 비율
thres = 0.7

np.random.seed(42)

G = nx.gnp_random_graph(n, p1, seed=42)
pos = nx.spring_layout(G)
ar = nx.adjacency_matrix(G)
ar = np.transpose(np.nonzero(ar))
graph = [[] for _ in range(n)]
for i, j in ar: graph[i].append(j)

def red_ratio(li):
    global color_map
    unique, counts = np.unique(color_map[li], return_counts=True)
    if 'red' not in unique: return 0
    return dict(zip(unique, counts))['red']/len(li)

def next_generation(): # return new color_map
    return np.array(['red' if red_ratio(i) > thres else 'blue' for i in graph])

color_map = np.random.choice(['blue', 'red'], size=n, p=[1-p2, p2])
options = {
    'node_color':color_map,
    'pos':pos,
    'node_size':40,
    'width':0.1
}

while loop<100:
    nx.draw(G, **options)
    color_map = next_generation()
    options['node_color'] = color_map
    if len(np.unique(color_map)) == 1:
        break
    # print(options['node_color'])
    plt.savefig(f'con_{i}.png')
    plt.clf()
    loop += 1