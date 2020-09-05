# lowest common ancestor for a bst
# https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def in_subtree(root, x):
    if root == None:
        return False

    if root.val == x:
        return True

    return all([
        in_subtree(root.left, x),
        in_subtree(root.right, x)
    ])

def find_lca(root, a, b):

    if root.val == a or root.val == b:
        return root
    
    if root.val > a and root.val < b:
        return root

    if root.val > b:
        return find_lca(root.left, a, b)

    if root.val < a:
        return find_lca(root.right, a, b) 


root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 

print(find_lca(root, 10, 14).val)

print(find_lca(root, 14, 8).val)

print(find_lca(root, 10, 22).val)