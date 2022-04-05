from __future__ import annotations
from functools import total_ordering
from dataclasses import dataclass, field
from collections import defaultdict
from typing import Any, DefaultDict, List


@total_ordering
@dataclass
class TNode:
    key: Any
    val: Any
    left: TNode = field(default=None, repr=False)
    right: TNode = field(default=None, repr=False)
    count: int = field(default=1)

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key


class BST:
    def __init__(self):
        self.root = None

    def size(self) -> int:
        return self.__size(self.root)

    def __size(self, node: TNode) -> int:
        if node is None:
            return 0
        return node.count

    def put(self, key: Any, val: Any) -> None:
        self.root = self.__put(self.root, key, val)

    def __put(self, root: TNode, key: Any, val: Any) -> TNode:
        node: TNode = TNode(key, val)
        if root is None:
            return node
        if node < root:
            root.left = self.__put(root.left, key, val)
        elif node > root:
            root.right = self.__put(root.right, key, val)
        else:
            root.val = val
        root.count = 1 + self.__size(root.left) + self.__size(root.right)
        return root

    def rank(self, key: Any) -> int:
        """How make keys are less than k"""
        return self.__rank(self.root, key)

    def __rank(self, root: TNode, key: Any) -> int:
        if root is None:
            return 0
        temp: TNode = TNode(key, None)
        if temp < root:
            return self.__rank(root.left, key)
        elif temp > root:
            return 1 + self.__size(root.left) + self.__rank(root.right, key)
        else:   # temp == root
            return self.__size(root.left)

    def min(self) -> Any:
        return self.__min(self.root)

    def __min(self, node: TNode) -> Any:
        if node is None:
            return node
        if node.left is None:
            return node
        return self.__min(node.left)

    def max(self) -> Any:
        return self.__max(self.root)

    def __max(self, node: TNode) -> Any:
        if node is None:
            return node

        if node.right is None:
            return node
        return self.__max(node.right)

    def floor(self, key: Any) -> Any:
        node: TNode = self.__floor(self.root, key)
        if node is None:
            return node
        return node.key

    def __floor(self, node: TNode, key: Any) -> TNode:
        """
        Case 1: [If key equals to key of root]
        The floot is of key is key

        Case 2: [if key is less than key at the root]
        the floor of key in the left subtree

        Case 3: [if key is greater than key at the root]
        the floor is in right subtree
        (if there is any key <= key in right sub tree)
        otherwise it is the key in the root

        """
        temp = TNode(key, key)
        if node is None:
            return node
        if temp == node:
            return node
        elif temp < node:
            return self.__floor(node.left, key)

        new_node = self.__floor(node.right, key)
        if new_node is not None:
            return new_node
        else:
            return node

    def ceil(self, key: Any) -> Any:
        node: TNode = self.__ceil(self.root, key)
        if node is None:
            return None
        return node.key

    def __ceil(self, node: TNode, key: Any) -> TNode:
        if node is None:
            return node
        temp: TNode = TNode(key, key)
        if temp == node:
            return node
        elif temp > node:
            return self.__ceil(node.right, key)

        new_node = self.__ceil(node.left, key)
        if new_node is not None:
            return new_node
        else:
            return node

    def vertical_order(self) -> DefaultDict[List[str]]:
        order_map = defaultdict(list)
        self.__vertical_order(self.root, 0, order_map)
        return order_map

    def __vertical_order(self, root, order, order_map) -> None:
        if root is None:
            return
        order_map[order].append(root)
        self.__vertical_order(root.left, order - 1, order_map)
        self.__vertical_order(root.right, order + 1, order_map)


if __name__ == "__main__":
    import sys
    bst = BST()
    for line in sys.stdin:
        key, value = list(map(lambda x: int(x) if x.isdigit() else x, line.split()))
        bst.put(key, value)

    """
                6
            /       \
           3        10
         /   \     /   \
        1    5    8     12
         \  /    / \
          2 4   7   9
    """
    print(f"Size: {bst.size()}")
    print(f"Rank(e): {bst.rank('e')}")
    print(f"Rank(x): {bst.rank('x')}")
    print(f"Min: {bst.min()}")
    print(f"Max: {bst.max()}")
    print(f"Floor(g): {bst.floor('g')}")
    print(f"Floor(q): {bst.floor('q')}")
    print(f"Ceil(q): {bst.ceil('q')}")
    import pprint
    pprint.pprint(bst.vertical_order())

