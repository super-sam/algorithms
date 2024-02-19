public class Selection {
    public static void sort(Comparable[] items){
        int N = items.length;
        for (int i =0; i < N-1; i++){
            int min = i+1;
            for (int j = i+1; j < N; j++){
                if(less(items[j], items[i])){
                    min = j;
                }
                exchange(items, i, min);
            }
        }
    }

    public static boolean less(Comparable a, Comparable b){
        return a.compareTo(b) < 0;
    }

    public static void exchange(Comparable[] items, int i, int j){
        Comparable temp = items[i];
        items[i] = items[j];
        items[j] = temp;
    }

    public static void main(String[] args){
        int[] items = {5, 4, 3, 2, 1};
        Selection.sort(items);
        System.out.println(items);
    }
}