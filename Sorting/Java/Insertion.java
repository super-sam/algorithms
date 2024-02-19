public class Insertion {
    public static void sort(Comparable[] items) {
        int N = items.length;
        for (int i = 1; i < N; i++) {
            for (int j = i; j > 0 && less(items[j], items[j - 1]); j--) {
                exchange(items, j, j - 1);
            }
        }
    }

    public static boolean less(Comparable a, Comparable b) {
        return a.compareTo(b) < 0;
    }

    public static void exchange(Comparable[] items, int i, int j) {
        Comparable temp = items[i];
        items[i] = items[j];
        items[j] = temp;
    }

    public static void main(String[] args) {
        Integer[] items = {5, 4, 3, 2, 1}; // Changed to Integer[] to match Comparable type
        Insertion.sort(items);
        for (int i : items) {
            System.out.print(i + " ");
        }
    }
}