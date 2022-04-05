from functools import total_ordering
from typing import Any

@total_ordering
class Edge:
    def __init__(self, v: int, w: int, weight: float):
        self.__v = v
        self.__w = w
        self.__weight =  weight

    def either(self) -> int:
        return self.__v

    def other(self, v: int) -> int:
        if v == self.__v:
            return self.__w
        return self.__v

    @property
    def weight(self):
        return self.__weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return f"{self.__v} - {self.__w} : {self.weight}"
    
    def __repr__(self) -> str:
        return f"Edge({self.__v}, {self.__w}, {self.weight})"

class MinPQ:
    def __init__(self, num: int) -> None:
        self.pq = []
    
    def left_child_idx(self, parent_idx: int) -> int:
        return 2 * parent_idx + 1
    
    def right_child_idx(self, parent_idx: int) -> int:
        return 2 * parent_idx + 2
    
    def parent_idx(self, child_idx: int) -> int:
        return (child_idx - 1) // 2
    
    def has_left_child(self, parent_idx: int) -> bool:
        return self.left_child_idx(parent_idx) < len(self.pq)
    
    def has_right_child(self, parent_idx: int) -> bool:
        return self.right_child_idx(parent_idx) < len(self.pq)
    
    def has_parent(self, child_idx: int) -> bool:
        return self.parent_idx(child_idx) >= 0
    
    def left_child(self, parent_idx):
        if not self.has_left_child(parent_idx):
            raise IndexError(f"left child doesn't exist for {parent_idx}")
        return self.pq[self.left_child_idx(parent_idx)]
    
    def right_child(self, parent_idx):
        if not self.has_right_child(parent_idx):
            raise IndexError(f"right child doesn't exist for {parent_idx}")
        return self.pq[self.right_child_idx(parent_idx)]
    
    def parent(self, child_idx: int) -> Any:
        if not self.has_parent(child_idx):
            raise IndexError(f"parent doesm't exist for {child_idx}")
        return self.pq[self.parent_idx(child_idx)]
    
    def exch(self, i: int, j: int) -> None:
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
    
    def heapify_up(self, index: int) -> None:
        if not self.valid_idx(index):
            raise IndexError(f"{index} is not a valid index")
        while self.has_parent(index) and self.pq[index] < self.parent(index):
            self.exch(index, self.parent_idx(index))
            index = self.parent_idx(index)
    
    def heapify_down(self, index: int) -> None:
        if not self.valid_idx(index):
            raise IndexError(f"{index} is not a valid index")
        
        while self.has_left_child(index):
            smallest_idx = self.left_child_idx(index)
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smallest_idx = self.right_child_idx(index)
            if self.pq[index] < self.pq[smallest_idx]:
                break
            self.exch(index, smallest_idx)
            index = smallest_idx


    def heappush(self, item: Any) -> None:
        self.pq.append(item)
        self.heapify_up(len(self.pq) - 1)

    def heappop(self) -> Any:
        self.exch(0, -1)
        item = self.pq.pop()
        if len(self.pq):
            self.heapify_down(0)
        return item

    def valid_idx(self, index: int) -> bool:
        return 0 <= index < len(self.pq)

class IndexMinPQ(MinPQ):
    def __init__(self, num: int) -> None:
        """ Create indexex priority queue with indices 0, num - 1"""
        super().__init__(num)
        # self.pq = []                  # index of key in the heap position
        self.keys = [None] * num        # is the priority of index
        self.qp = [-1] * num          # is the heap position of the key with index

    def exch(self, i: int, j: int) -> None:
        super().exch(i, j)
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j
    
    def heappush(self, index: int, key: Any):
        """Associate key with index"""
        super().heappush(index)
        self.qp[index] = len(self.pq) - 1
        self.keys[index] = key 

    def decrease_key(self, index: int, key: Any):
        """Decrease the key of associated with index"""
        pass

    def contains(self, index: int) -> bool:
        """Is index in the priority queue"""
        pass

    # def heappop(self) -> int:
    #     """Remove the minimal key and return its associated index"""
    #     pass

    def is_empty(self) -> bool:
        """Is the priority queue empty"""
        pass

    def size(self) -> int:
        """Number of entries in the priority queue"""
        pass

if __name__ == "__main__":
    '''
    A B 6
    B C 1
    A C 4
    B D 5
    C D 7
    D E 7
    D F 10
    F E 2
    '''
    # min_pq = IndexMinPQ(8)
    # min_pq.heappush(Edge('A', 'B', 6))
    # min_pq.heappush(Edge('B', 'C', 1))
    # min_pq.heappush(Edge('A', 'C', 4))
    # min_pq.heappush(Edge('B', 'D', 5))
    # min_pq.heappush(Edge('C', 'D', 7))
    # min_pq.heappush(Edge('D', 'E', 7))
    # min_pq.heappush(Edge('D', 'F', 10))
    # min_pq.heappush(Edge('F', 'E', 2))
    # print(min_pq.pq)
    # while min_pq.pq:
    #     print(min_pq.heappop())

    strings = ["it", "was", "the", "best", "of", "times", "it", "was", "the", "worst"]
    # min_pq = MinPQ(len(strings))
    # for index in range(len(strings)):
    #     min_pq.heappush(strings[index])
    # print(min_pq.pq)
    # while min_pq.pq:
    #     print(min_pq.heappop())


    indexmin_pq = IndexMinPQ(4)
    for index in range(4):
        indexmin_pq.heappush(index, strings[index])
    print(indexmin_pq.pq)
    print(indexmin_pq.qp)
    print(indexmin_pq.keys)