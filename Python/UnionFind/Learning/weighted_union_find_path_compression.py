import sys
from typing import List


class WeightedUnionFindPC:
    def __init__(self, n: int):
        self.ids: List[int, str] = []
        self.size: List[int, str] = []

        for i in range(n):
            self.ids.append(i)
            self.size.append(1)

    def __root(self, index) -> int:
        while index != self.ids[index]:
            self.ids[index] = self.ids[self.ids[index]]
            index = self.ids[index]
        return index

    def union(self, p: int, q: int) -> None:
        root_p = self.__root(p)
        root_q = self.__root(q)

        if self.size[root_p] < self.size[root_q]:
            self.ids[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        else:
            self.ids[root_q] = root_p
            self.size[root_p] += self.size[root_q]

    def connected(self, p: int, q: int) -> bool:
        return self.__root(p) == self.__root(q)


if __name__ == "__main__":
    n: int = int(sys.stdin.readline())
    wufpc: WeightedUnionFindPC = WeightedUnionFindPC(n)
    for line in sys.stdin:
        p, q = map(int, line.split())
        if not wufpc.connected(p, q):
            wufpc.union(p, q)
            print(f"{p} is connected with {q}", wufpc.ids)

    print(f"4 and 1 connected: {wufpc.connected(4, 1)}")
    print(f"8 and 9 connected: {wufpc.connected(8, 9)}")
    wufpc.union(1, 4)
    print(f"4 and 1 connected: {wufpc.connected(4, 1)}")
