from typing import Any, List
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


class Selection:
    @staticmethod
    @timetaken
    def sort(items: Any):
        n = len(items)
        for i in range(n-1):
            min_index = i
            for j in range(i+1, n):
                if Selection.less(items[j], items[min_index]):
                    min_index = j
            Selection.exchange(items, i, min_index)

    @staticmethod
    def less(a: Any, b: Any) -> bool:
        return a < b

    @staticmethod
    def exchange(items: List, i, j):
        items[i], items[j] = items[j], items[i]


if __name__ == '__main__':
    items: List[int] = [random.randint(0, 50000) for x in range(20000)]
    Selection.sort(items)
    Selection.sort(items)

