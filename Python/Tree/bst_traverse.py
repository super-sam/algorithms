from Tree import bst_base
from collections import deque
from typing import List


class BST(bst_base.BST):
    def dfs(self) -> List[bst_base.Node]:
        dfs_list = []
        self.__dfs(self.root, dfs_list)
        return dfs_list

    def __dfs(self, root: bst_base.Node, dfs_list: List[bst_base.Node]) -> None:
        if root is None:
            return

        self.__dfs(root.left, dfs_list)
        dfs_list.append(root)
        self.__dfs(root.right, dfs_list)

    def dfs_reverse(self) -> List[bst_base.Node]:
        dfs_list = []
        self.__dfs_reverse(self.root, dfs_list)
        return dfs_list

    def __dfs_reverse(self, root: bst_base.Node, dfs_list: List[bst_base.Node]) -> None:
        if root is None:
            return
        self.__dfs_reverse(root.right, dfs_list)
        dfs_list.append(root)
        self.__dfs_reverse(root.left, dfs_list)

    def bfs(self) -> List[bst_base.Node]:
        bfs_list = []
        self.__bfs(self.root, bfs_list)
        return bfs_list

    def __bfs(self, root: bst_base.Node, bfs_list: List[bst_base.Node]) -> None:
        if root is None:
            return
        nodes = deque()
        nodes.append(root)
        while nodes:
            node = nodes.popleft()
            bfs_list.append(node)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

    def __iter__(self):
        dfs_list: List[bst_base.Node] = self.dfs()
        for node in dfs_list:
            yield node


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
       a    r
        /  \
         c h
            \
        \   /
             m
    """
    print(bst.min())
    print(bst.max())
    print(bst.dfs())
    print(bst.dfs_reverse())
    print(bst.bfs())
    for node in bst:
        print(node)