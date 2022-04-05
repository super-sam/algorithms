from typing import Any, List
import copy
from Sorting import shuffling, utils


class Merge:
    @staticmethod
    @utils.timetaken
    def sort(items: List[Any], order: str = "ASC"):
        low = 0
        high = len(items) - 1
        Merge.__sort(items, low, high, order)

    @staticmethod
    def __sort(items: List[Any], low: int=0, high: int=None, order: str = "ASC"):
        if low < high:
            mid: int = (high + low) // 2
            Merge.__sort(items, low, mid, order)
            Merge.__sort(items, mid+1, high, order)
            Merge.combine(items, low, mid, high, order)

    @staticmethod
    def combine(items: List[Any], low: int, mid: int, high: int, order: str= "ASC") -> None:
        operator: str = ">" if order.upper() == "DSC" else "<"
        left_sorted: List[Any] = copy.deepcopy(items[low: mid+1])
        right_sorted: List[Any] = copy.deepcopy(items[mid+1: high + 1])
        left_index = 0
        right_index = 0
        k = low
        while k <= high:
            if left_index < len(left_sorted) and right_index < len(right_sorted):
                if eval(f"{left_sorted[left_index]} {operator} {right_sorted[right_index]}"):
                    items[k] = left_sorted[left_index]
                    left_index += 1
                else:
                    items[k] = right_sorted[right_index]
                    right_index += 1
                k += 1
            else:
                break
        while left_index < len(left_sorted):
            items[k] = left_sorted[left_index]
            left_index += 1
            k += 1

        while right_index < len(right_sorted) :
            items[k] = right_sorted[right_index]
            right_index += 1
            k += 1


if __name__ == "__main__":
    items = [x for x in range(50000)]
    shuffeled_items = shuffling.shuffle(items)
    Merge.sort(shuffeled_items, order="DSC")
    Merge.sort(shuffeled_items)
    print(shuffeled_items)
