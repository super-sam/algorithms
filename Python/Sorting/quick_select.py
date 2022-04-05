from Sorting import quick
from Sorting import shuffling
from typing import Any, List


class QuickSelect:
    @staticmethod
    def select(items: List[Any], k: int) -> Any:
        k = k - 1
        shuffling.shuffle(items)
        lo: int = 0
        hi: int = len(items) - 1
        while hi > lo:
            p: int = quick.Quick.partition(items, lo, hi)
            if p < k:
                lo = p + 1
            elif p > k:
                hi = p - 1
            else:
                return items[p]
        return items[p]


if __name__ == "__main__":
    items = [1, 20, 40, 2, 3, 50, 5, 6, 7, 8, 9, 10]
    fiftyth = QuickSelect.select(items, 4)
    print(fiftyth)