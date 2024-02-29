from typing import List


class Quick:
    @staticmethod
    def partition(items: List[int], lo: int, hi: int) -> int:
        pivot = lo
        left, right = lo+1, hi

        while True:
            while items[left] < items[pivot]:
                left += 1
                if left == hi:
                    break
            while items[right] > items[pivot]:
                right -= 1
                if right == lo:
                    break

            if left >= right:
                break
            items[left], items[right] = items[right], items[left]
        items[pivot], items[right] = items[right], items[pivot]

        return right
    
    
    @staticmethod
    def _sort(items: List[int], lo: int, hi: int):
        if lo >= hi:
            return
        p = Quick.partition(items, lo,  hi)
        Quick._sort(items, lo, p-1)
        Quick._sort(items, p+1, hi)
    
    @staticmethod
    def sort(items: List[int]):
        Quick._sort(items, 0, len(items) - 1)


if __name__ == "__main__":
    items = [10, 4, 9 , 3 , 2 ,5, 1, 6]
    QuickSort.sort(items)
    print(items)

