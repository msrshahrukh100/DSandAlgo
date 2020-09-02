# https://www.geeksforgeeks.org/reverse-a-linked-list/


class Node:
    def __init__(self, val, nex):
        self.val = val
        self.next = nex


def create_linkedlist(l):
    head = p = None
    for i in l:
        node = Node(i, None)
        if not head:
            p = head = node
        else:
            p.next = node
            p = node
    
    return head

def print_linkedlist(head):
    p = head
    while p:
        print(p.val)
        p = p.next


def reverse_linkedlist(head):

    current = head
    prev = next = None

    while current:
        next = current.next
        current.next = prev

        prev = current
        current = next
    
    return prev

def main():
    head = create_linkedlist([1, 2, 3, 4, 5, 6])
    print_linkedlist(head)
    print_linkedlist(reverse_linkedlist(head))


main()