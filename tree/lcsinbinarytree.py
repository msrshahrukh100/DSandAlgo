# find lca in bst
#  https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def find_path(root, k, path):
    if root == None:
        return False

    if root.val == k:
        path.append(root.val)
        return path
    np = path[:]
    np.append(root.val)
    return find_path(root.left, k, np) or find_path(root.right, k, np)


def find_lca(root, a, b):
    p1 = find_path(root, a, [])
    p2 = find_path(root, b, [])
    i = 0
    while i < len(p1) and i < len(p2):
        if p1[i] != p2[i]:
            return p1[i-1]
        if p1[i] in [a, b]:
            return p1[i]
        i += 1


def find_lca_better(root, a, b):
    
    if root == None:
        return None

    if root.val == a or root.val == b:
        return root.val
    
    ls = find_lca_better(root.left, a, b)
    rs = find_lca_better(root.right, a, b)

    if ls and rs:
        return root.val
    
    return ls or rs
    

    
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 

print(find_path(root, 6, []))


print("LCA(4, 5) = %d" %(find_lca_better(root, 4, 5))) 
print("LCA(4, 6) = %d" %(find_lca_better(root, 4, 6))) 
print("LCA(3, 4) = %d" %(find_lca_better(root, 3, 4)))
print("LCA(2, 4) = %d" %(find_lca_better(root, 2, 4)))
  
