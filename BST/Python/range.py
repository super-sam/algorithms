from bst import BSTNode, root
from select import select
from rank import rank

def range(root: BSTNode, low: int, high: int) -> int:
    """
    Both inclusive
    """
    if root is None:
        return 0
    if select(root, high):
        return rank(root, high) - rank(root, low) + 1
    return rank(root, high) - rank(root, low)

def range2(root: BSTNode, low: int, high: int) -> int:
    """
    Both inclusive
    """
    if root is None:
        return 0
    
    result = rank(root, high) - rank(root, low)
    if select(root, low):
        result -= 1
    return result

if __name__ == "__main__":
    print(range(root, 5, 15))  # 3
    print(range(root, 6, 16))  # 4
    print(range2(root, 5, 15))  # 3
    print(range2(root, 6, 15))  # 3
    print(range2(root, 5, 16))  # 4
    print(range2(root, 6, 16))  # 4