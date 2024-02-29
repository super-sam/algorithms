import ramdom


from typing import List

def shuffle(items: List[int]) -> None:
    for i in range(len(items)):
        r = random.randint(0, i)
        items[r], items[i] = items[i], items[r]