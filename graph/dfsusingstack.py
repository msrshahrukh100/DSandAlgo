from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, root):

        stack = []
        stack.append(root)
        visited = [False] * len(self.graph)
        visited[root] = True

        while len(stack) != 0:
            e = stack.pop()
            print(e)

            for i in self.graph[e]:
                if not visited[i]:
                    visited[i] = True
                    stack.append(i)

g = Graph() 
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 
  
print("Following is DFS from (starting from vertex 2)") 
g.dfs(2) 