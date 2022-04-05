import sys
from typing import List


class QU:
    def __init__(self, n: int):
        self.ids: List[int] = []
        for i in range(n):
            self.ids.append(i)

    def __root(self, index):
        while index != self.ids[index]:
            index = self.ids[index]
        return index

    def union(self, p: int, q: int) -> None:
        root_p = self.__root(p)
        root_q = self.__root(q)
        self.ids[root_p] = self.ids[root_q]

    def connected(self, p: int, q: int) -> bool:
        return self.__root(p) == self.__root(q)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    qu: QU = QU(n)

    for line in sys.stdin:
        p, q = map(int, line.split())
        if not qu.connected(p, q):
            qu.union(p, q)
            print(f"{p} connected with {q}")

    print(f"4 and 1 connected: {qu.connected(4, 1)}")
    print(f"8 and 9 connected: {qu.connected(8, 9)}")
    qu.union(1, 4)
    print(f"4 and 1 connected: {qu.connected(4, 1)}")