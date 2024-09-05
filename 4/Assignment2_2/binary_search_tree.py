class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert(node.right, value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def inorder_traversal(self, node, values):
        if node:
            self.inorder_traversal(node.left, values)
            values.append(node.value)
            self.inorder_traversal(node.right, values)
        return values

bst = BinarySearchTree()

bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(5)
bst.insert(15)
bst.insert(25)
bst.insert(35)

found_node = bst.search(15)
print("Found Node:", found_node.value if found_node else "Not Found")  
print("Inorder Traversal:", bst.inorder_traversal(bst.root, []))

