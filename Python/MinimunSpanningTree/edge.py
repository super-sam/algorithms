from functools import total_ordering

@total_ordering
class Edge:
    def __init__(self, v: int, w: int, weight: float):
        self.__v = v
        self.__w = w
        self.__weight: weight

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
