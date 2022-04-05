from typing import Any, List
from Sorting import shuffling


class Quick:
    @staticmethod
    def sort(items: List[Any]) -> None:
        shuffling.shuffle(items)
        Quick.__sort(items, 0, len(items) - 1)

    @staticmethod
    def __sort(items: List[Any], lo: int, hi: int) -> None:
        if lo <= hi:
            p = Quick.partition(items, lo, hi)
            Quick.__sort(items, lo, p - 1)
            Quick.__sort(items, p + 1, hi)

    @staticmethod
    def partition(items: List[Any], lo: int, hi: int) -> int:
        """Returns the partion key left of which has smaller items and right of which has greater items
      Returns:
          A partion key
      """
        i: int = lo
        j: int = hi

        while True:
            while items[i] < items[lo]:
                i += 1
                if i == hi:
                    break

            while items[j] >= items[lo]:
                j -= 1
                if j == lo:
                    break

            if i >= j:
                break
            items[i], items[j] = items[j], items[i]
        items[lo], items[j] = items[j], items[lo]

        return j


if __name__ == "__main__":
    items = [x for x in range(10)]
    shuffling.shuffle(items)
    Quick.sort(items)
    print(items)
