from bst import BSTNode, root


def inorder_traversal(node: BSTNode):
    path = []
    if node is None:
        return path
    
    def dfs(node: BSTNode):
        if node.left:
            dfs(node.left)
        path.append(node.value)
        if node.right:
            dfs(node.right)
    dfs(node)
    return path


if __name__ == "__main__":
    assert inorder_traversal(root) == [0, 1, 3, 5, 7, 10, 13, 15, 17]
    assert inorder_traversal(None) == []
    print(inorder_traversal(root))  # [3, 5, 7, 10, 13, 15, 17]