# Tree - Node class


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def print_val(self):
        print(self.val)
        if self.left is not None:
            self.left.print_val()
        if self.right is not None:
            self.right.print_val()






