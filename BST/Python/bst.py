class BSTNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.value)

root = BSTNode(10)
root.left = BSTNode(5)
root.right = BSTNode(15)
root.left.left = BSTNode(3)
root.left.right = BSTNode(7)
root.right.left = BSTNode(13)
root.right.right = BSTNode(17)
root.left.left.left = BSTNode(1)
root.left.left.left.left = BSTNode(0)