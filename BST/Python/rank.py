from bst import BSTNode

from typing import Optional

def rank(root: Optional[BSTNode], value: int) -> int:
    if root is None:
        return 0
    
    def rank_util(node: Optional[BSTNode]):
        if node is None:
            return 0
        if value < node.value:
            return rank_util(node.left)
        elif value > node.value:
            return 1 + size(node.left) + rank_util(node.right)
        else:
            return size(node.left)
    
    return rank_util(root)

    
def size(node: Optional[BSTNode]) -> int:
    if node is None:
        return 0
    return 1 + size(node.left) + size(node.right)




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

    # print(rank(root, 10))  # 4
    print(rank(root, 7))  # 4
    print(rank(root, 15))  # 4