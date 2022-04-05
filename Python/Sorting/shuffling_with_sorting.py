from typing import Any, List
import random
from functools import total_ordering
from dataclasses import dataclass
import shell
import insertion

@dataclass
@total_ordering
class ShuffleItem:
    key: float
    value: Any

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key


def shuffle(items: List[Any]):
    shuffle_items = [ShuffleItem(random.random(), x) for x in items]
    insertion.Insertion.sort(shuffle_items)
    return [s_item.value for s_item in shuffle_items]


if __name__ == "__main__":
    items = [i for i in range(10)]
    shuffled_items = shuffle(items)
