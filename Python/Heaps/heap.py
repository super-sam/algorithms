from typing import Any, List
from abc import ABC, abstractmethod


class Heap(ABC):
    def __init__(self, items: List[Any] = None):
        self._items: List[Any] = items or []

    @abstractmethod
    def heapify_up(self):
        pass

    @abstractmethod
    def heapify_down(self):
        pass

    @staticmethod
    def get_parent_index(child_index: int) -> int:
        return (child_index - 1) // 2

    @staticmethod
    def get_left_child_index(parent_index: int) -> int:
        return 2*parent_index + 1

    @staticmethod
    def get_right_child_index(parent_index: int) -> int:
        return 2*parent_index + 2

    @staticmethod
    def has_parent(child_index) -> bool:
        return Heap.get_parent_index(child_index) >= 0

    @staticmethod
    def has_left_child(items, parent_index) -> bool:
        return Heap.get_left_child_index(parent_index) < len(items)

    def has_right_child(self, parent_index) -> bool:
        return self.get_right_child_index(parent_index) < len(self._items)

    def parent(self, child_index: int) -> Any:
        if not self._items or not self.has_parent(child_index):
            raise IndexError
        return self._items[self.get_parent_index(child_index)]

    def left_child(self, parent_index: int) -> Any:
        if not self._items or not self.has_left_child(parent_index):
            raise IndexError
        return self._items[self.get_left_child_index(parent_index)]

    def right_child(self, parent_index: int) -> Any:
        if not self._items or not self.has_right_child(parent_index):
            raise IndexError
        return self._items[self.get_right_child_index(parent_index)]

    def swap(self, index1, index2):
        self._items[index1], self._items[index2] = self._items[index2], self._items[index1]

    def add(self, item: Any) -> None:
        self._items.append(item)
        self.heapify_up()

    def pop(self) -> Any:
        if not self._items:
            raise IndexError
        self.swap(0, len(self._items) - 1)
        item = self._items.pop()
        self.heapify_down()
        return item


class MinHeap(Heap):
    def heapify_up(self, index: int = None) -> None:
        index = index or len(self._items) - 1
        while self.has_parent(index) and self.parent(index) > self._items[index]:
            self.swap(index, self.get_parent_index(index))
            index = self.get_parent_index(index)

    def heapify_down(self, index: int = 0) -> None:
        while self.has_left_child(index):
            smallest_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self._items[smallest_index] > self.right_child(index):
                smallest_index = self.get_right_child_index(index)
            if self._items[index] > self._items[smallest_index]:
                self.swap(index, smallest_index)
                index = smallest_index
            else:
                break


class MaxHeap(Heap):
    def heapify_up(self, index: int = None) -> None:
        index = index or len(self._items) - 1
        while self.has_parent(index) and self.parent(index) < self._items[index]:
            self.swap(index, self.get_parent_index(index))
            index = self.get_parent_index(index)

    def heapify_down(self, index: int = 0):
        while self.has_left_child(index):
            largest_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.right_child(index) > self._items[largest_index]:
                largest_index = self.get_right_child_index(index)
            if self._items[largest_index] > self._items[index]:
                self.swap(largest_index, index)
                index = largest_index
            else:
                break

class HeapSort:
    @staticmethod
    def heapify(items: List[Any]) -> None:
        for index in range((len(items) - 1) // 2, -1, -1):


if __name__ == "__main__":
    import random
    min_heap = MinHeap()
    max_heap = MaxHeap()
    for _ in range(10):
        min_heap.add(random.randint(1, 100))
        max_heap.add(random.randint(1, 100))
        print(min_heap._items, max_heap._items)

    print(min_heap.pop(), max_heap.pop())
    print(min_heap.pop(), max_heap.pop())
    print(min_heap.pop(), max_heap.pop())
    print(min_heap.pop(), max_heap.pop())
    print(min_heap.pop(), max_heap.pop())
    print(min_heap.pop(), max_heap.pop())



