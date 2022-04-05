from typing import Any, List


class Binary:
    @staticmethod
    def search(items: List[Any], item: Any) -> int:
        """In a sorted array, find the index of the item"""
        return  Binary.search_recursive(items, item, 0, len(items) - 1)

    @staticmethod
    def search_recursive(items: List[Any], item: Any, lo: int, hi: int) -> int:
        if lo > hi:
            return -1
        mid = (lo + hi) // 2
        if item == items[mid]:
            return mid
        elif item < items[mid]:
            return Binary.search_recursive(items, item, lo, mid - 1)
        else:
            return Binary.search_recursive(items, item, mid + 1, hi)


if __name__ == "__main__":
    import sys
    items = []
    for line in sys.stdin:
        items.append(int(line))

    assert Binary.search(items, items[0]) == 0
    assert Binary.search(items, items[-1]) == len(items) - 1
    assert Binary.search(items, items[3]) == 3
