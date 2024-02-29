from typing import List


class MergeSort:
    @staticmethod
    def merge(arr: List[int], lo: int, mid: int, hi: int) -> None:
        left_sorted: List[int] = arr[lo: mid+1]
        right_sorted: List[int] = arr[mid+1: hi+1]
        left_idx, right_idx = 0, 0
        k = lo
        while k <= hi:
            if left_idx >= len(left_sorted) or right_idx >= len(right_sorted):
                break
            if left_sorted[left_idx] < right_sorted[right_idx]:
                arr[k] = left_sorted[left_idx]
                left_idx += 1
            else:
                arr[k] = right_sorted[right_idx]
                right_idx += 1
            k += 1
        while left_idx < len(left_sorted):
            arr[k] = left_sorted[left_idx]
            k += 1
            left_idx += 1
        while right_idx < len(right_sorted):
            arr[k] = right_sorted[right_idx]
            k += 1
            right_idx += 1
    
    @staticmethod
    def _sort(arr: List[int], lo, hi):
        if lo >= hi:
            return
        mid: int = (hi + lo) // 2
        MergeSort._sort(arr, lo, mid)
        MergeSort._sort(arr, mid + 1, hi)
        MergeSort.merge(arr, lo, mid, hi)
    
    @staticmethod
    def sort(arr: List[int]) -> None:
        MergeSort._sort(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    items = [10, 4, 9 , 3 , 2 ,5, 1, 6]
    MergeSort.sort(items)
    print(items)
