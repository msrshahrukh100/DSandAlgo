from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, v):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(v)

        while len(queue) != 0:
            now = queue.pop(0)
            print(now, end=" -> ")
            visited[now] = True
            for i in self.graph[now]:
                if not visited[i]:
                    queue.append(i)




g = Graph() 
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 
  
print("Following is BFS from (starting from vertex 2)") 
g.bfs(2) 
# print(g.graph[2])