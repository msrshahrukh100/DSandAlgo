
from collections import defaultdict

class Node:
    
    num_of_nodes = 1

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.__class__.num_of_nodes += 1


ancestors = defaultdict(list)

def bfs(root):
    queue = []
    visited = [False] * Node.num_of_nodes
    visited[root.val] = True
    queue.append(root)

    while len(queue) != 0:
        m = queue.pop(0)
        print(m.val)
        if m.left and not visited[m.left.val]:
            visited[m.left.val] = True
            queue.append(m.left)
            ancestors[m.left.val] = [m.val] + ancestors[m.val]
        
        if m.right and not visited[m.right.val]:
            visited[m.right.val] = True
            queue.append(m.right)
            ancestors[m.right.val] = [m.val] + ancestors[m.val]


root = Node(1); 
root.left = Node(2); 
root.right = Node(3); 
root.left.left = Node(4); 
root.left.right = Node(5); 
root.right.left = Node(6); 
root.right.right = Node(7); 
root.left.right.left = Node(8); 
root.left.right.right = Node(9); 

a, b = 4, 9  

bfs(root)    
print(ancestors)

a1 = ancestors[4]
a2 = ancestors[9]

for i in a1:
    if i in a2:
        print("The answer is %s " % i)
        break

# for k, v in ancestors.items():
#     print("Ancestors of %s are %s" % (k, v))