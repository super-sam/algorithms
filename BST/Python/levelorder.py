from bst import BSTNode, root
from collections import deque

def level_order(root: BSTNode):
    result = []
    if root is None:
        return result
    
    queue = deque([root, None])
    level = []
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(level)
            level = []
            if queue:
                queue.append(None)
        else:
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result

if __name__ == "__main__":
    print(level_order(root))  # [[10], [5, 15], [3, 7, 13, 17], [1], [0]]