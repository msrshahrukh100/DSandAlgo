# all paths from source to destination
# https://www.geeksforgeeks.org/print-paths-given-source-destination-using-bfs/

from collections import defaultdict

class Graph:
    def __init__(self, v):
        self.graph = defaultdict(list)
        self.v = v
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, start, dest, path, recursed):
        
        queue = []
        visited = [False] * self.v
        queue.append(start)
        visited[start] = True
        recursed[start] = True

        if start == dest:
            path.append(dest)
            print("One of the path is %s" % path)
        path.append(start)

        while len(queue) != 0:
            m = queue.pop(0)

            for i in self.graph[m]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
                    if not recursed[i]:
                        self.bfs(i, dest, path[:], recursed)
        

g = Graph(4)

g.add_edge(0, 3) 
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 3) 
g.add_edge(2, 0) 
g.add_edge(2, 1)
recursed = [False] * g.v
g.bfs(2, 3, [], recursed)