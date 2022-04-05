from __future__ import annotations
from collections import defaultdict, deque
from typing import DefaultDict, List
from Tree import bst_traverse


class BST(bst_traverse.BST):
    def min(self) -> bst_traverse.Node:
        if self.root is None:
            return self.root
        return self.__min(self.root)

    def __min(self, root: bst_traverse.Node) -> bst_traverse.Node:
        if root.left is None:
            return root
        return self.__min(root.left)

    def max(self) -> bst_traverse.Node:
        if self.root is None:
            return self.root
        return self.__max(self.root)

    def __max(self, root: bst_traverse.Node) -> bst_traverse.Node:
        if root.right is None:
            return root
        return self.__max(root.right)

    def rank(self, key: str) -> int:
        return self._rank(self.root, key)

    def _rank(self, root: bst_traverse.Node, key: str) -> int:
        if root is None:
            return 0
        if key < root.key:
            return self._rank(root.left, key)
        elif key > root.key:
            return 1 + self._size(root.left) + self._rank(root.right, key)
        else:
            return self._size(root.left)

    def height(self) -> int:
        return self.__height(self.root)

    def __height(self, root: bst_traverse.Node) -> int:
        if root is None:
            return -1
        return 1 + max(self.__height(root.left), self.__height(root.right))

    def vertical_order(self) -> DefaultDict[int, List[str]]:
        order_map = defaultdict(list)
        nodes = deque()
        nodes.append((self.root, 0))
        while nodes:
            node, order = nodes.popleft()
            order_map[order].append(node)
            if node.left:
                nodes.append((node.left, order - 1))
            if node.right:
                nodes.append((node.right, order + 1))
        return order_map

    def __contains__(self, key: str) -> bool:
        return not self.select(key) is None

    def select(self, key: str) -> bst_traverse.Node:
        return self.__select(self.root, key)

    def __select(self, root: bst_traverse.Node, key: str) -> bst_traverse.Node:
        if root is None:
            return root
        if key < root.key:
            return self.__select(root.left, key)
        elif key > root.key:
            return self.__select(root.right, key)
        else:
            return root

    def del_min(self) -> None:
        if self.root is None:
            raise IndexError

        self.root = self.__del_min(self.root)

    def __del_min(self, root: bst_traverse.Node) -> bst_traverse.Node:
        if root.left is None:
            return root.right
        root.left = self.__del_min(root.left)
        root.count = 1 + self._size(root.left) + self._size(root.right)
        return root

    def del_max(self) -> None:
        if self.root is None:
            raise IndexError

        self.root = self.__del_max(self.root)

    def __del_max(self, root: bst_traverse.Node) -> bst_traverse.Node:
        if root.right is None:
            return root.left
        root.right = self.__del_max(root.right)
        root.count = 1 + self._size(root.left) + self._size(root.right)
        return root

    def del_node(self, node: bst_traverse.Node) -> None:
        self.root = self.__del_node(self.root, node)

    def __del_node(self, root: bst_traverse.Node, node: bst_traverse.Node) -> bst_traverse.Node:
        if root is None:
            return root

        if node < root:
            root.left = self.__del_node(root.left, node)
        elif node > root:
            root.right = self.__del_node(root.right, node)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            temp: Node = root
            root = self.__min(temp.right)
            root.right = self.__del_min(temp.right)
            root.left = temp.left

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
    print(bst.min())
    print(bst.max())
    print(bst.height())
    print(bst.vertical_order())
    bst.del_min()
    print(bst.min())
    bst.del_max()
    print(bst.max())
    e_node = bst.select('e')
    print(e_node)
    print(bst.dfs())
    bst.del_node(e_node)
    print(bst.dfs())
