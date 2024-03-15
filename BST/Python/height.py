from bst import BSTNode


def height(root: BSTNode):
    if root is None:
        return 0
    def height_util(node: BSTNode):
        if node is None:
            return 0
        return 1 + max(height_util(node.left), height_util(node.right))
    
    return height_util(root)


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

    assert height(root) == 5, "Height of the tree is 3"
    assert height(None) == 0