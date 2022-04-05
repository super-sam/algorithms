from typing import Any, List
import random


def shuffle(items: List[Any]):
    for i in range(len(items)):
        random_index = random.randint(0, i)
        items[random_index], items[i] = items[i], items[random_index]

    return items


if __name__ == "__main__":
    items = [i for i in range(10)]
    shuffled_items = shuffle(items)
    print(shuffled_items)
