from bst import BSTNode


def size(root: BSTNode):
    if root is None:
        return 0
    
    def size_util(node: BSTNode) -> int:
        if node is None:
            return 0
        return 1 +size_util(node.left) + size_util(node.right)
    return size_util(root)


if __name__ == "__main__":
    root = BSTNode(10)
    root.left = BSTNode(5)
    root.right = BSTNode(15)
    root.left.left = BSTNode(3)
    root.left.right = BSTNode(7)
    root.right.left = BSTNode(13)
    root.right.right = BSTNode(17)
    root.left.left.left = BSTNode(1)
    root.left.left.left.left = BSTNode(0)

    print(size(root))
    assert size(root) == 9, "Size of the tree is 8"