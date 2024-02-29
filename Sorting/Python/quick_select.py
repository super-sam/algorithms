from typing import List


class QuickSelect:
    @staticmethod
    def partion(items: List[int], lo: int, hi: int) -> int:
        pivot = lo
        left, right = lo, hi

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
    def select(items: List[int], k: int):
        k = len(items) - k
        lo, hi = 0, len(items) - 1
        while hi > lo:
            p = QuickSelect.partion(items, lo, hi)
            if p == k: return items[p:]
            elif p < k:
                lo = p + 1
            else:
                hi = p - 1
        return items[p:] 


if __name__ == "__main__":
    items = [1, 20, 40, 2, 3, 50, 5, 6, 7, 8, 9, 10]
    fiftyth = QuickSelect.select(items, 2)
    print(fiftyth)