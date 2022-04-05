import math
from typing import List


def min_coins(coins: List[int], sum_value: int) -> int:
    """Return the number of coins required to get the sum value"""
    table = [math.inf for _ in range(sum_value + 1)]
    table[0] = 0

    for value in range(1, sum_value + 1):
        for coin in range(len(coins)):
            if coins[coin] <= value:
              sub_min = table[value - coins[coin]]
              if sub_min + 1 < table[value]:
                  table[value] = sub_min + 1
            print(table, coins[coin], value)
    print(table)
    if table[sum_value] == math.inf:
        return -1
    return table[sum_value]


if __name__ == "__main__":
    coins = [1, 3, 5]
    sum_value = 11
    print(min_coins(coins, sum_value))
