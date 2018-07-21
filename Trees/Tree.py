# Generate a simple tree structure.

from Trees.Node import Node

root = Node("rootNode")
leftNode = Node("leftNode")
leftNode2 = Node("leftNode2")

rightNode = Node("rightNode")
rightNode2 = Node("rightNode2")

root.left = leftNode
root.right = rightNode

leftNode.left = leftNode2
leftNode.right = rightNode2

root.print_val()

