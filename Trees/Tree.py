# Generate a simple tree structure.

from Trees.Node import Node

root = Node("rootNode")
leftNode = Node("leftNode")
leftNode2 = Node("leftNode2")

rightNode = Node("rightNode")
rightNode2 = Node("rightNode2")

nodel3 = Node("node Level 3")

root.left = leftNode
root.right = rightNode

leftNode.left = leftNode2
leftNode.right = rightNode2

rightNode2.left = nodel3



root.print_val()

