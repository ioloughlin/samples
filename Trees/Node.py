# Tree - Node class


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.indentLevel = ""

    def print_val(self):
        if self.left is not None:
            print(self.indentLevel + " " + self.val)
            self.left.indentLevel = self.indentLevel + "L"
            self.left.print_val()
        if self.right is not None:
            print(self.indentLevel + " " + self.val)
            self.right.indentLevel = self.indentLevel + "R"
            self.right.print_val()
        if self.left is None and self.right is None:
            print(self.indentLevel + " leaf " + self.val)







