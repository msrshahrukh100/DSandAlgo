from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs_util(self, i, visited):
        visited[i] = True
        print(i)

        for v in self.graph[i]:
            if not visited[v]:
                self.dfs_util(v, visited)

    def dfs(self):
        V = len(self.graph)
        visited = [False] * V

        for i in range(V):
            if not visited[i]:
                self.dfs_util(i, visited)


g = Graph() 
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 
  
print("Following is Depth First Traversal")
g.dfs() 