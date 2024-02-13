from typing import List

def max_profit(weights: List[int], values: List[int], capacity: int):

    def max_profit_util(capacity: int, nsize: int) -> int:
        if capacity == 0 or nsize == 0:
            return 0
        if weights[nsize] > capacity:
            return max_profit_util(capacity, nsize-1)
        else:
            return max(
                max_profit_util(capacity, nsize-1), 
                values[nsize] + max_profit_util(capacity - weights[nsize], nsize-1)
            )
    return max_profit_util(capacity, len(weights) - 1)

def max_profit_memo(weights: List[int], values: List[int], capacity: int):
    """
    Recursive with memorisation
    Memorise the value that are changing. i.e. size of capacity and size
    """
    memo = [[-1 for _ in range(capacity+1)] for _ in range(len(weights))]
    pprint(memo)
    def max_profit_util(capacity: int, nsize: int) -> int:
        if capacity == 0 or nsize == 0:
            return 0
        if memo[nsize][capacity] != -1:
            pprint(memo)
            return memo[nsize][capacity]
        
        if weights[nsize] > capacity:
            memo[nsize][capacity] = max_profit_util(capacity, nsize-1)
        else:
            memo[nsize][capacity] = max(
                max_profit_util(capacity, nsize-1), 
                values[nsize] + max_profit_util(capacity - weights[nsize], nsize-1)
            )
        pprint(memo)
        return memo[nsize][capacity]
    return max_profit_util(capacity, len(weights) - 1)
        
if __name__ == '__main__':
    print(max_profit([1, 3, 4, 5], [1, 4, 5, 7], 7))