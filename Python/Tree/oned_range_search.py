"""
Range Searching
- How many keys are between a and b
- What are the keys between a and b
"""
from typing import Any, List
from Tree import red_black_tree


class BST(red_black_tree.RBT):
    def range_count(self, lo: str, hi: str) -> int:
        if hi in self:
            return self.rank(hi) - self.rank(lo) + 1
        else:
            return self.rank(hi) - self.rank(lo)

    def range_search(self, lo: str, hi: str) -> List[red_black_tree.Node]:
        dfs_list = []
        self.__range_search(self.root, lo, hi, dfs_list)
        return dfs_list

    def __range_search(self, root, lo: str, hi: str, dfs_list: List[Any]) -> None:
        if root is None:
            return

        if root.key >= lo:
            self.__range_search(root.left, lo, hi, dfs_list)
        if lo <= root.key <= hi:
            dfs_list.append(root)
        if root.key <= hi:
            self.__range_search(root.right, lo, hi, dfs_list)


if __name__ == "__main__":
    bst = BST()
    bst.put('s', 's')
    bst.put('e', 'e')
    bst.put('a', 'a')
    bst.put('r', 'r')
    bst.put('x', 'x')
    bst.put('c', 'c')
    bst.put('h', 'h')
    bst.put('m', 'm')

    print(bst.rank('f'))
    print(bst.range_count('f', 't'))
    print(bst.range_search('f', 't'))
    print(bst.range_search('b', 'd'))
