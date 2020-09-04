from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, root):
        queue = []
        queue.append(root)
        visited = [False] * (len(self.graph))
        visited[root] = True
        while len(queue) != 0:
            e = queue.pop(0)
            print(e)
            for i in self.graph[e]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)


g = Graph() 
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 
  
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
g.bfs(2) 
