from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Node:
    char: str
    val: Any = field(default=None)
    left: Node = field(default=None, repr=False)
    mid: Node = field(default=None, repr=False)
    right: Node = field(default=None, repr=False)

class TST:
    def __init__(self) -> None:
        self.root = None
    
    def put(self, key: str, val: Any) -> None:
        self.root = self.__put(self.root, key, val, 0)

    def __put(self, node: Node, key: str, val: Any, idx: int) -> Node:
        char: int = ord(key[idx])
        if node == None:
            node = Node(char)
        if char < node.char:
            node.left = self.__put(node.left, key, val, idx)
        elif char > node.char:
            node.right = self.__put(node.right, key, val, idx)
        elif idx < len(key) - 1:
            node.mid = self.__put(node.mid, key, idx + 1)
        else:
            node.val = val
        return node
    
    def get(self, key):
        node = self.__get(self.root, key, 0)
        if node is None:
            return None
        return node.val
    
    def __get(self, node, key, idx):
        if node is None:
            return None
        char: str = ord(key[idx])
        if char < node.char:
            return self.__get(node.left, key, idx)
        elif char > node.char:
            return self.__get(node.right, key, idx)
        elif idx < len(key) - 1:
            return self.__get(node.mid, key, idx + 1)
        else:
            return node

