import sys


class WeightedUnionFind:
    def __init__(self, n):
        self.ids = []
        self.size = []
        for i in range(n):
            self.ids.append(i)
            self.size.append(1)

    def __root(self, index):
        while index != self.ids[index]:
            index = self.ids[index]

        return index

    def connected(self, p: int, q: int):
        return self.__root(p) == self.__root(q)

    def union(self, p: int, q: int):
        size_p = self.size[p]
        size_q = self.size[q]
        root_p = self.__root(p)
        root_q = self.__root(q)
        if size_p < size_q:
            self.ids[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        else:
            self.ids[root_q] = root_p
            self.size[root_p] += self.size[root_q]


if __name__ == "__main__":
    n: int = int(sys.stdin.readline())
    wuf: WeightedUnionFind = WeightedUnionFind(n)
    for line in sys.stdin:
        p, q = map(int, line.split())
        if not wuf.connected(p, q):
            wuf.union(p, q)
            print(f"{p} is connected with {q}", wuf.ids)

    print(f"4 and 1 connected: {wuf.connected(4, 1)}")
    print(f"8 and 9 connected: {wuf.connected(8, 9)}")
    wuf.union(1, 4)
    print(f"4 and 1 connected: {wuf.connected(4, 1)}")