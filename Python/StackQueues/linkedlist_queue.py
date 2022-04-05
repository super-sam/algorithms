from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
import queue_abstract

class LinkedListQueue(queue_abstract.QueueAbstract):
    __first: Node = None
    __last: Node = None

    @dataclass
    class Node:
        info: Any
        next: Node = field(repr=False, default=None)
    
    def is_empty(self) -> bool:
        return self.__first == None
    
    def get(self) -> Any:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.__first.info
    
    def enque(self, item: Any) -> None:
        node: Node = self.Node(item)
        if self.is_empty():
            self.__first = node
        else:
            self.__last.next = node
            
        self.__last = node
    
    def deque(self) -> Any:
        item = self.get()
        self.__first = self.__first.next
        if self.is_empty():
            self.__last = self.__last.next
        return item

