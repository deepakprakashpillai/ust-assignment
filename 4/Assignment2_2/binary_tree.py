class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def inorder_traversal(self, node, values):
        if node:
            self.inorder_traversal(node.left, values)
            values.append(node.value)
            self.inorder_traversal(node.right, values)
        return values

    def preorder_traversal(self, node, values):
        if node:
            values.append(node.value)
            self.preorder_traversal(node.left, values)
            self.preorder_traversal(node.right, values)
        return values

    def postorder_traversal(self, node, values):
        if node:
            self.postorder_traversal(node.left, values)
            self.postorder_traversal(node.right, values)
            values.append(node.value)
        return values

bt = BinaryTree()

bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(3)
bt.insert(7)
bt.insert(12)
bt.insert(18)

print("Inorder Traversal:", bt.inorder_traversal(bt.root, []))

print("Preorder Traversal:", bt.preorder_traversal(bt.root, []))

print("Postorder Traversal:", bt.postorder_traversal(bt.root, []))