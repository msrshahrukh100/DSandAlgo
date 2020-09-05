# https://www.geeksforgeeks.org/in-place-convert-a-given-binary-tree-to-doubly-linked-list/
# my solution seems better


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class DllNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def binaryTreeToDll(root, is_right):

    if not root:
        return None
    

    dll_node = DllNode(root.val)
    dll_node.prev = binaryTreeToDll(root.left, False)
    dll_node.next = binaryTreeToDll(root.right, True)

    if dll_node.prev:
        dll_node.prev.next = dll_node
    if dll_node.next:
        dll_node.next.prev = dll_node

    if is_right:
        return dll_node.prev or dll_node
    
    return dll_node.next or dll_node

def eval_print(head):
    p = head
    while p.prev:
        p = p.prev
    
    last = p
    while p:
        print(p.val)
        last = p
        p = p.next

    print("In reverse order")
    while last:
        print(last.val)
        last = last.prev


root = Node(10) 
root.left = Node(12) 
root.right = Node(15) 
root.left.left = Node(25) 
root.left.right = Node(30) 
root.right.left = Node(36)

head = binaryTreeToDll(root, True)

eval_print(head)


