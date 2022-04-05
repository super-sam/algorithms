from collections import deque
from tkinter import N
from typing import Any, Final


class Node:
    def __init__(self, n) -> None:
        self.val = None
        self.next = [None] * n


class RwayTries:
    N: Final = 256
    root: Node = Node(N)

    def put(self, key: str, val: Any) -> None:
        self.root = self.__put(self.root, key, val, 0)

    def __put(self, node: Node, key: str, val: Any, idx: int) -> Node:
        if node is None:
            node =  Node(self.N)
        if idx == len(key):
            node.val = val
            return node
        char: int = ord(key[idx])
        node.next[char] = self.__put(node.next[char], key, val, idx + 1)
        return node
    
    def get(self, key: str) -> Any:
        return self.__get(self.root, key, 0)

    def __get(self, node: Node, key: str, idx: int) -> Any:
        if node is None:
            return None
        if idx == len(key):
            return node.val
        char: int = ord(key[idx])
        return self.__get(node.next[char], key, idx + 1)
    
    def keys(self):
        words = deque()
        self.collect(self.root, "", words)
        return words
    
    def collect(self, node, prefix, words):
        if node is None:
            return
        if node.val != Node:
            words.append(prefix)
        for num in range(N):
            self.collect(node.next[num], prefix + chr(num), words``)


if __name__ == '__main__':
    value = "sea"
    tries = RwayTries()
    tries.put(value, 1)
    print(tries.get("she"))    
    print(tries.get("sea"))