# https://www.geeksforgeeks.org/bipartite-graph/

from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
        self.v = 0
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.v = max(self.v, u, v)
    
    def bfs(self, root):
        visited = [False] * self.v
        colors = [None] * self.v
        queue = []
        visited[root] = True
        colors[root] = 1

        while len(queue) != 0:
            m = queue.pop(0)
            print(m)
            now_color = colors[root]

            for i in self.graph[m]:
                if not visited[i]:
                    if colors[i] == now_color:
                        return False
                    colors[i] = 2 if now_color == 1 else 1
                    visited[i] = True
                    queue.append(i)


