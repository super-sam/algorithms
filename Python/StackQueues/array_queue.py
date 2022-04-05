from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, List
import queue_abstract

@dataclass
class ArrayQueue(queue_abstract.QueueAbstract):
    __first: int = field(repr=False, default=0)
    __last: int = field(repr=False, default=0)
    __queue: List[Any] = []

    def is_empty(self) -> bool:
        return len(self.__queue) == 0
    
    def is_full(self) -> bool:
        return len(self.__queue) == self.__last
    
    def get(self) -> Any:
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.__queue[self.__first]
    
    def enque(self, item: Any) -> None:
        
        if self.is_full():
            increment: int = len(self.__queue) or 1
            self.__queue.extend([None]*increment)
        
        
