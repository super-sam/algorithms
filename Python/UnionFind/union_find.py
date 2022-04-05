from logging import root


class UF:
    def __init__(self, n) -> None:
        self.__ids = [idx for idx in range(n)]
        self.__size = [1] * n
    
    def __root(self, idx) -> bool:
        while idx != self.__ids[idx]:
            self.__ids[idx] = self.__ids[self.__ids[idx]]
            idx = self.__ids[idx]
        return idx
    
    def is_connected(self, p, q) -> bool:
        return self.__root(p) == self.__root(q)
    
    def union(self, p, q) -> None:
        root_p = self.__root(p)
        root_q = self.__root(q)

        if self.__size[root_p] < self.__size[root_q]:
            self.__ids[root_p] = root_q
            self.__size[root_q] = self.__size[root_p]
        else:
            self.__ids[root_q] = root_p
            self.__size[root_p] = self.__size[root_q]
