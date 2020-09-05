# topological sort
# https://www.geeksforgeeks.org/topological-sorting/

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.v = 0
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.v = max(self.v, v, u)
    
    def dfs_util(self, u, visited):
        visited[u] = True
        print(u)
        for i in self.graph[u]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, root):

        visited = [False] * (self.v + 1)

        # for i in self.graph[root]:
        #     if not visited[i]:
        self.dfs_util(root, visited)
    
    def topological_sort_util(self, u, visited, stack):
        visited[u] = True

        for i in self.graph[u]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        
        # insert it at the beginning like stack = [u] + stack
        #  or do stack.insert(0, v)
        # or print the reverse of stack in final answer
        stack.insert(0, u) 

    def topological_sort(self, stack, u):
        visited = [False] * (self.v + 1)
        for u in range(self.v + 1):
            if not visited[u]:
                self.topological_sort_util(u, visited, stack)
        # self.topological_sort_util(u, visited, stack)

g= Graph() 
g.add_edge(5, 2); 
g.add_edge(5, 0); 
g.add_edge(4, 0); 
g.add_edge(4, 1); 
g.add_edge(2, 3); 
g.add_edge(3, 1); 

g.dfs(5)
stack = []
g.topological_sort(stack, 5)
print("The topological sort is %s " % stack)