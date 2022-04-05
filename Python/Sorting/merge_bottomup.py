from typing import Any, List
from Sorting import shuffling
import copy
from Sorting import utils


class MergeBU:
    @staticmethod
    def combine(items: List[Any], low: int, mid: int, high: int, order: str = "ASC") -> None:
        # print(low, mid, high, end=" ")
        operator: str = ">" if order.upper() == "DSC" else "<"
        left_sorted: List[Any] = copy.deepcopy(items[low: mid + 1])
        right_sorted: List[Any] = copy.deepcopy(items[mid + 1: high + 1])
        # print(left_sorted, right_sorted, end=" ")
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

        while right_index < len(right_sorted):
            items[k] = right_sorted[right_index]
            right_index += 1
            k += 1

    @staticmethod
    @utils.timetaken
    def sort(items: List[Any]) -> None:
        size = 1
        while size < len(items):
            low = 0
            while low < len(items) - size:
                high = min(low + size + size - 1, len(items) - 1)
                mid = low + size - 1
                MergeBU.combine(items, low, mid, high)
                low += size + size
                # print(items)
            size += size


if __name__ == "__main__":
    items = [x for x in range(10)]
    shuffeled_items = shuffling.shuffle(items)
    MergeBU.sort(shuffeled_items)
    print(shuffeled_items)
