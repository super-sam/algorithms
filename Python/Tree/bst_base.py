from __future__ import annotations
from dataclasses import dataclass, field
from functools import total_ordering
from typing import Any


@dataclass
@total_ordering
class Node:
    key: str
    val: Any
    left: Node = field(default=None, repr=False)
    right: Node = field(default=None, repr=False)
    count: int = field(default=1)

    def __eq__(self, __o: object) -> bool:
        return self.key == __o.key

    def __lt__(self, __o: object) -> bool:
        return self.key < __o.key


class BST:
    def __init__(self) -> None:
        self.root = None

    def size(self) -> int:
        return self._size(self.root)

    def _size(self, root: Node) -> int:
        if root is None:
            return 0
        return root.count

    def put(self, key: str, val: Any) -> None:
        self.root = self.__put(self.root, key, val)

    def __put(self, root: Node, key: str, val: Any) -> Node:
        if root is None:
            return Node(key, val)

        if key < root.key:
            root.left = self.__put(root.left, key, val)
        elif key > root.key:
            root.right = self.__put(root.right, key, val)
        else:
            root.val = val

        root.count = 1 + self._size(root.left) + self._size(root.right)
        return root


if __name__ == "__main__":
    import sys

    bst = BST()
    for line in sys.stdin:
        key, value = list(map(lambda x: int(x) if x.isdigit() else x, line.split()))
        bst.put(key, value)

    """
            s
          /    \
         e      x
        /  \
       a    r
        \   /
         c h
            \
             m
    """
