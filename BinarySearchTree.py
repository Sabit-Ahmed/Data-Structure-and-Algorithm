class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:

    def insert(self, node, key) -> Node:
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        if node.right is not None:
            print(node.right.key)
        return node


def main():
    bst = BinarySearchTree()
    root = None
    root = bst.insert(root, 8)
    root = bst.insert(root, 3)
    root = bst.insert(root, 1)
    root = bst.insert(root, 6)
    root = bst.insert(root, 7)
    root = bst.insert(root, 10)
    root = bst.insert(root, 14)
    root = bst.insert(root, 4)
    print(root.key)

if __name__ == "__main__":
    main()
