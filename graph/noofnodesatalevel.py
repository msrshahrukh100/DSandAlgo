# count number of nodes at a level 
# https://www.geeksforgeeks.org/count-number-nodes-given-level-using-bfs/

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.v = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.v = max(self.v, u, v)

    def bfs(self, root):
        queue = []
        visited = [False] * (self.v + 1) 

        queue.append(root)
        visited[root] = True
        level_of_nodes = [0] * (self.v + 1) 
        while len(queue) != 0:
            m = queue.pop(0)
            print(m)

            for i in self.graph[m]:
                if not visited[i]:
                    level_of_nodes[i] = level_of_nodes[m] + 1
                    visited[i] = True
                    queue.append(i)
    
        print(level_of_nodes, self.v)

g = Graph() 
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
  
  
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
g.bfs(0) 