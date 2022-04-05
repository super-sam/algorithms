from typing import List, Any
import random


def timetaken(fn):
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(f"Time Taken: {end - start} sec")
        return result
    return wrapper


class Insertion:
    @staticmethod
    @timetaken
    def sort(items: List[Any]):
        for i in range(len(items)):
            for j in range(i, 0, -1):
                if Insertion.less(items[j], items[j-1]):
                    Insertion.exchange(items, j, j-1)
                else:
                    break


    @staticmethod
    def less(a: Any, b: Any) -> bool:
        return a < b

    @staticmethod
    def exchange(items: List, i, j):
        items[i], items[j] = items[j], items[i]


if __name__ == '__main__':
    items: List[int] = [random.randint(0, 50000) for x in range(20000)]
    Insertion.sort(items)
    Insertion.sort(items)
