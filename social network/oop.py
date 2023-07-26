import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pprint
import os

np.random.seed(42)

class CN:
    def __init__(self, n, p1, p2, thres):
        self.n = n
        self.p1 = p1
        self.p2 = p2
        self.thres = thres
        self.G = nx.gnp_random_graph(n, p1, seed=42)
        self.graph = [[] for _ in range(n)]
        for i, j in np.transpose(np.nonzero(nx.adjacency_matrix(self.G))): self.graph[i].append(j)
        self.color_map = np.random.choice(['blue', 'red'], size=n, p=[1-p2, p2])
        self.options = {
            'node_color':self.color_map,
            'pos':nx.spring_layout(self.G),
            'node_size':40,
            'width':0.1
        }

    def red_ratio(self, li):
        unique, counts = np.unique(self.color_map[li], return_counts=True)
        if 'red' not in unique: return 0
        return dict(zip(unique, counts))['red']/len(li)
    
    def next_color_map(self): # return new color_map
        return np.array(['red' if self.red_ratio(i) > self.thres else 'blue' for i in self.graph])

    def draw(self):
        nx.draw(self.G, **self.options)

    def next_generation(self):
        self.color_map = self.next_color_map()
        self.options['node_color'] = self.color_map

    def break_det(self):
        if len(np.unique(self.color_map)) == 1:
            print(np.unique(self.color_map)[0])
            return True

    def simulation(self, num):
        loop = 0
        while loop<100:
            self.draw()
            plt.savefig(f'./imgs/imgs_{int(10*self.thres)}/img_{num}/con_class_{loop}.png')
            plt.clf()
            if self.break_det():
                return (np.unique(self.color_map)[0], loop)
            self.next_generation()
            loop += 1
        return ('k', 0)

# CN1 = CN(100, 0.12, 0.6, 0.51)

for j in np.linspace(0, 1, num=11):
    num = 50
    cnt = 0
    result = []
    steps = []

    for i in np.linspace(0, 1, num=num):
        C = CN(100, 0.12, i, j)
        re = C.simulation(cnt)
        result.append(re[0][0])
        steps.append(re[1])
        cnt += 1

    plt.clf()
    plt.scatter(np.linspace(0, 1, num=num), steps, c=result)
    plt.xlabel('1$ = 1won ratio')
    plt.ylabel('step')
    plt.savefig(f'./graph/graph_{int(10*j)}.png')
