from __future__ import annotations
from dataclasses import dataclass
from lib2to3.pytree import Node
from typing import Any
import stack_abstract

class LinkedList(stack_abstract.StackAbstract):
    __top: Node = None

    @dataclass
    class Node:
        info: Any
        next: Node = None
    
    def is_empty(self) -> bool:
        return self.__top == None

    def peek(self) -> Any:
        item: Any = None

        if not self.is_empty():
            item = self.__top.info
        return item
    
    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        item: Any = self.peek()
        self.__top = self.__top.next
        return item
    
    def push(self, item: Any) -> None:
        node: Node = self.Node(item)
        node.next = self.__top
        self.__top = node


if __name__ == '__main__':
    linkedList: LinkedList = LinkedList()
    linkedList.push("1")
    linkedList.push("2")
    linkedList.push("3")
    print(linkedList.is_empty())
    print(linkedList.pop())
    print(linkedList.pop())
    print(linkedList.pop())
    print(linkedList.is_empty())

    linkedListInt: LinkedList = LinkedList()
    linkedListInt.push(1)
    linkedListInt.push(2)
    linkedListInt.push(3)
    print(linkedListInt.is_empty())
    print(linkedListInt.pop())
    print(linkedListInt.pop())
    print(linkedListInt.pop())
    print(linkedListInt.is_empty())
    print(linkedListInt.pop())