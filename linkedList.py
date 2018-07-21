# Linked List Python example code


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing


node1 = Node(12)
node2 = Node(99)
node3 = Node(37)
node1.next = node3 # 12->99
node3.next = node2 # 99->37

print(node1.val)
print(node1.next.val)
print(node1.next.next.val)
