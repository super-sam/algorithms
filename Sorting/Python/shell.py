from typing import Any, List

class Shell:
    @staticmethod
    def less(this: Any, that: any) -> bool:
        return this < that
    @staticmethod
    def exch(items: List[Any], i: int, j: int) -> None:
        items[i], items[j] = items[j], items[i]
    
    @staticmethod
    def sort(items: List[Any]) -> None:
        h=0
        while h < len(items) // 3:
            h = h*3 + 1
        while h > 0:
            for i in range(1, len(items)):
                for j in range(i, 0, -h):
                    if not Shell.less(items[j], items[j-h]):
                        break
                    Shell.exch(items, j, j-h)
            
            h = h // 3

if __name__ == "__main__":
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    random.shuffle(arr)
    Shell.sort(arr)
    print(arr)