"""
This Sorting technique is used in place of regular quick sort when there are duplicate keys
"""
from typing import Any, List
from Sorting import shuffling


class QuickThree:
    @staticmethod
    def sort(items: List[Any]):
        shuffling.shuffle(items)
        lo: int = 0
        hi: int = len(items) - 1
        return QuickThree.__sort(items, lo, hi)

    @staticmethod
    def __sort(items: List[Any], lo: int, hi: int):
        if lo < hi:
            lt: int = lo
            gt: int = hi
            i: int = lo + 1
            p_element: Any = items[lo]
            while i <= gt:
                if items[i] < p_element:
                    items[i], items[lt] = items[lt], items[i]
                    i += 1
                    lt += 1
                elif items[i] > p_element:
                    items[i], items[gt] = items[gt], items[i]
                    gt -= 1
                else:
                    i += 1
            QuickThree.__sort(items, lo, lt - 1)
            QuickThree.__sort(items, gt + 1, hi)


if __name__ == "__main__":
    items = [1, 20, 40, 2, 3, 50, 5, 6, 7, 8, 9, 10]
    # items = ["P", "A", "B", "X", "W", "P", "P", "V", "P", "D", "P", "C", "D", "Y", "Z"]
    QuickThree.sort(items)
    print(items)

