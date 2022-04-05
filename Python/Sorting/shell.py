from typing import List, Any
from Sorting import shuffling


def timetaken(fn):
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(f"Time Taken: {end - start} sec")
        return result
    return wrapper


class Shell:
    @staticmethod
    @timetaken
    def sort(items: List[Any]):
        h = 1
        while h < len(items)//3:
            h = h*3 + 1
        while h > 0:
            for i in range(len(items)):
                for j in range(i, 0, -h):
                    if Shell.less(items[j], items[j - h]):
                        Shell.exchange(items, j, j - h)
                    else:
                        break
            h = h // 3
    @staticmethod
    def less(a: Any, b: Any) -> bool:
        return a < b
    @staticmethod
    def exchange(items: List[Any], i: int, j: int):
        items[j], items[i] = items[i], items[j]


if __name__ == '__main__':
    items: List[int] = [x for x in range(10000)]
    shuffled_items = shuffling.shuffle(items)
    Shell.sort(shuffled_items)
    print(items)
