from __future__ import annotations
from dataclasses import dataclass, field
from functools import total_ordering
from typing import Any
import enum
from Tree import bst


class Color(enum.Enum):
    RED: bool = True
    BLACK: bool = False


@total_ordering
@dataclass
class Node:
    key: Any
    val: Any
    color: bool = field(default=Color.RED.value)
    count: int = field(default=1)
    left: TNode = field(default=None, repr=False)
    right: TNode = field(default=None, repr=False)

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key


class RBT(bst.BST):
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

        if RBT.is_red(root.right) and not RBT.is_red(root.left):
            root = self.rotate_left(root)
        if RBT.is_red(root.left) and RBT.is_red(root.left.left):
            root = self.rotate_right(root)
        if RBT.is_red(root.left) and RBT.is_red(root.right):
            RBT.flip_color(root)

        root.count = 1 + self._size(root.left) + self._size(root.right)
        return root

    @staticmethod
    def is_red(node: Node) -> bool:
        if node is None:
            return False
        return node.color == Color.RED.value

    def rotate_left(self, node: Node) -> Node:
        next_node: Node = node.right
        node.right = next_node.left
        next_node.left = node
        next_node.color = node.color
        node.color = Color.RED.value
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return next_node

    def rotate_right(self, node: Node) -> Node:
        next_node: Node = node.left
        node.left = next_node.right
        next_node.right = node
        next_node.color = node.color
        node.color = Color.RED.value
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return next_node

    @staticmethod
    def flip_color(node: Node) -> None:
        node.color = Color.RED.value
        node.left.color = Color.BLACK.value
        node.right.color = Color.BLACK.value


if __name__ == "__main__":
    import sys
    rbt = RBT()
    for line in sys.stdin:
        key, value = list(map(lambda x: int(x) if x.isdigit() else x, line.split()))
        rbt.put(key, value)
    print(rbt.dfs())
    m_node = rbt.select('e')
    # print(m_node, m_node.left, m_node.right)
