import sys
from UnionFind import weighted_union_find_path_compression


class Percolation:
    def __init__(self, n: int):
        self.n = n
        item_count = n * n
        self.sites: weighted_union_find_path_compression.WeightedUnionFindPC = \
            weighted_union_find_path_compression.WeightedUnionFindPC(item_count + 2)
        self.opened_sites = [False] * (n * n)
        self.open_sites = 0
        top_index = self.n * self.n
        bottom_index = self.n * self.n + 1
        for i in range(n):
            self.sites.union(top_index, i)
            self.sites.union(bottom_index, self.index_from(n-1, i))

    def _is_valid_point(self, row: int, col: int) -> bool:
        if row < 0 or row >= self.n or col < 0 or col >= self.n:
            return False
        return True

    def index_from(self, row: int, col: int):
        if row < 0 or row >= self.n or col < 0 or col >= self.n:
            raise IndexError("Out of bound")

        return row * self.n + col

    def open(self, row: int, col: int) -> None:
        """ Checks Opens the site at (row, col) """
        index: int = self.index_from(row, col)
        self.opened_sites[index] = True
        self.open_sites += 1

        if self._is_valid_point(row - 1, col) and self.is_open(row - 1, col):
            top_index = self.index_from(row - 1, col)
            self.sites.union(index, top_index)
        if self._is_valid_point(row, col + 1) and self.is_open(row, col + 1):
            right_index = self.index_from(row, col + 1)
            self.sites.union(index, right_index)
        if self._is_valid_point(row + 1, col) and self.is_open(row + 1, col):
            bottom_index = self.index_from(row + 1, col)
            self.sites.union(index, bottom_index)
        if self._is_valid_point(row, col - 1) and self.is_open(row, col - 1):
            left_index = self.index_from(row, col - 1)
            self.sites.union(index, left_index)

    def is_open(self, row: int, col: int) -> bool:
        """ Checks if the site(row, col) is open? """
        index = self.index_from(row, col)
        return self.opened_sites[index]

    def is_full(self, row: int, col: int) -> bool:
        """is the site row, col full"""
        pass

    def number_of_open_site(self) -> int:
        """Returns number of open site"""
        return self.open_sites

    def percolates(self) -> bool:
        """If the system percolates"""
        top_index = self.n * self.n
        bottom_index = self.n * self.n + 1
        return self.sites.connected(top_index, bottom_index)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    percolation = Percolation(n)
    for line in sys.stdin:
        p, q = map(int, line.split())
        percolation.open(p, q)
    print(percolation.percolates())
