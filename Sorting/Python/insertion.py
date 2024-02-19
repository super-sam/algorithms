from typing import Any

class Insertion:
    @staticmethod
    def less(a: int, b: int) -> bool:
        return a < b
    
    @staticmethod
    def exch(items: Any, i: int, j: int) -> None:
        items[i], items[j] = items[j], items[i]
    
    @staticmethod
    def sort(items: Any) -> None:
        N = len(items)
        for i in range(N):
            for j in range(i, 0, -1):
                if not Insertion.less(items[j], items[j-1]):
                    break
                Insertion.exch(items, j, j-1)

if __name__ == '__main__':
    items = [5, 4, 3, 2, 1]
    Insertion.sort(items)
    print(items)

                
