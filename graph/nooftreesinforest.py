# trees in forests or no.of islands
# https://www.geeksforgeeks.org/count-number-trees-forest/

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.v = 0
    

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.v = max(self.v, u, v)
    
    def dfs_helper(self, i, visited):
        visited[i] = True
        print(i)
        for j in self.graph[i]:
            if not visited[j]:
                self.dfs_helper(j, visited)

    def dfs(self):
        visited = [False] * (self.v + 1)
        trees = 0
        for i in range(self.v):
            if not visited[i]:
                trees += 1
                self.dfs_helper(i, visited) 
        
        print("Number of tress in the forest are %s" % trees)


g = Graph() 
g.add_edge(0, 1)  
g.add_edge(0, 2)  
g.add_edge(3, 4) 
  
print("Following is Depth First Traversal")
g.dfs() 