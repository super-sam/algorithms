from bst import BSTNode, root
from typing import Optional



def select(root: BSTNode, value: int) -> Optional[BSTNode]:
    if root is None:
        return root
    if value < root.value:
        return select(root.left, value)
    elif value > root.value:
        return select(root.right, value)
    else:
        return root