class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BynarySearchTree:
    def __init__(self):
        self.root = None

    def __int__(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(Value)
            else:
                self._insert_recursive(current_node.right, value)

