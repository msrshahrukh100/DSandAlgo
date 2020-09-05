# check if mirror of itself
# https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/


class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


def check_is_mirror(r1, r2):
    if r1 == None and r2 == None:
        return True
    
    if (r1 == None and r2 != None) or (r2 == None and r1 != None):
        return False
    
    # if r1.val == r2.val:
    #     return all([
    #         True,
    #         check_is_mirror(r1.left, r2.right),
    #         check_is_mirror(r1.right, r2.left)
    #     ])
    if r1.val == r2.val:
        return check_is_mirror(r1.left, r2.right) and check_is_mirror(r1.right, r2.left)
    
    return False


root = Node(1) 
root.left = Node(2) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(4) 
root.right.left = Node(4) 
root.right.right = Node(3)

print(check_is_mirror(root, root))