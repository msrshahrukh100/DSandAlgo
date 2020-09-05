# https://www.geeksforgeeks.org/kth-ancestor-node-binary-tree-set-2/

from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
ancestors = defaultdict(list)

def kthancestors(root):

    queue = []
    visited = [False] * 6
    visited[root.val] = True
    queue.append(root)

    while queue:
        m = queue.pop(0)

        if m.left and not visited[m.left.val]:
            queue.append(m.left)
            visited[m.left.val] = True
            ancestors[m.left.val] = [m.val] + ancestors[m.val]
        if m.right and not visited[m.right.val]:
            queue.append(m.right)
            visited[m.right.val] = True
            ancestors[m.right.val] = [m.val] + ancestors[m.val] 

def printKthAncestor(n, k):
    if k <= len(ancestors[n]):
        print(ancestors[n][k-1])
    else:
        print("-1")

root = Node(1)  
root.left = Node(2)  
root.right = Node(3)  
root.left.left = Node(4)  
root.left.right = Node(5)  
kthancestors(root)

# for k, v in ancestors.items():
#     print("Ancestors of %s - %s" % (k, v))

printKthAncestor(5, 2)
printKthAncestor(5, 3)