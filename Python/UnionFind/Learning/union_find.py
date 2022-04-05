import sys


class UF:
    def __init__(self, n: int):
        self.ids = []
        for i in range(n):
            self.ids.append(i)

    def union(self, p: int, q: int) -> None:
        pid: int = self.ids[p]
        qid: int = self.ids[q]
        for i in range(len(self.ids)):
            if self.ids[i] == pid:
                self.ids[i] = qid

    def connected(self, p: int, q: int) -> bool:
        return self.ids[p] == self.ids[q]


if __name__ == '__main__':
    n: int = int(sys.stdin.readline())
    uf: UF = UF(n)
    for line in sys.stdin:
        p, q = map(int, line.split())
        if not uf.connected(p, q):
            uf.union(p, q)
            print(f"{p} connected with {q}")

    print(f"4 and 1 connected: {uf.connected(4, 1)}")
    print(f"8 and 9 connected: {uf.connected(8, 9)}")
    uf.union(1, 4)
    print(f"4 and 1 connected: {uf.connected(4, 1)}")