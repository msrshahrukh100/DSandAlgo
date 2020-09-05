# find the level with max number of nodes

# https://www.geeksforgeeks.org/level-maximum-number-nodes/


class Node:
    number_of_nodes = 0

    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None
        self.level = 0
        self.__class__.number_of_nodes += 1
    

number_of_nodes_at_level = []

def insert(index):
    if index < len(number_of_nodes_at_level):
        number_of_nodes_at_level[index] += 1
    else:
        number_of_nodes_at_level.append(1)

    print(number_of_nodes_at_level)


def print_levels(root):
    
    if root:
        print("Level of Node %s is %s " % (root.val, root.level))
        print_levels(root.left)
        print_levels(root.right)


def find_level_with_max_nodes(root):

    queue = []
    queue.append(root)
    number_of_nodes_at_level.append(1)


    while len(queue) != 0:
        m = queue.pop(0)

        if m.left:
            m.left.level = m.level + 1
            queue.append(m.left)
            insert(m.left.level)
        
        if m.right:
            m.right.level = m.level + 1
            queue.append(m.right)
            insert(m.right.level)
    
    return number_of_nodes_at_level.index(max(number_of_nodes_at_level))

root = Node(2)     #     2      
root.left     = Node(1)     #     / \  
root.right     = Node(3)     #     1     3      
root.left.left = Node(4)     # / \ \  
root.left.right = Node(6)     # 4     6 8  
root.right.right = Node(8) #     /      
root.left.right.left = Node(5)#  


print("Finally the answer is %s " % find_level_with_max_nodes(root))
print_levels(root)
# print(number_of_nodes_at_level)