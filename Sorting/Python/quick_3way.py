class QuickSortDuplicate:
    @staticmethod
    def exch(items, i, j):
        items[i], items[j] = items[j], items[i]
    
    @staticmethod
    def sort(items):
        QuickSortDuplicate._sort(items, 0, len(items) - 1)
    
    @staticmethod
    def _sort(items, lo, hi):
        if lo >= hi:
            return
        lt, gt = lo, hi
        i = lo + 1
        while i <= gt:
            if items[i] < items[lt]:
                items[i], items[lt] = items[lt], items[i]
                i += 1
                lt += 1
            elif items[i] > items[lt]:
                items[i], items[gt] = items[gt], items[i]
                gt -= 1
            else:
                i += 1
        QuickSortDuplicate._sort(items, lo, lt - 1)
        QuickSortDuplicate._sort(items, gt + 1, hi)

if __name__ == "__main__":
    items = [1, 20, 40, 3, 3, 5, 5, 6, 7, 8, 6, 1]
    QuickSortDuplicate.sort(items)
    print(items)