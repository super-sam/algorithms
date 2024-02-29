// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>
using namespace std;

class QuickSort{
    private:
        static void exch(vector<int> &items, int i, int j){
            int temp = items[i];
            items[i] = items[j];
            items[j] = temp;
        }
        static void sort(vector<int> &items, int lo, int hi){
            if (lo >= hi) return;
            int lt = lo, gt = hi, i = lo + 1;
            while (i <= gt){
                if (items[i] < items[lt])QuickSort::exch(items, i++, lt++);
                else if (items[i] > items[lt])QuickSort::exch(items, i, gt--);
                else i++;
            }
            QuickSort::sort(items, lo, lt-1);
            QuickSort::sort(items, gt+1, hi);
        }
    public:
        static void sort(vector<int> & items){
            QuickSort::sort(items, 0, items.size() -1);
        }
};

int main() {
    // Write C++ code here
    std::cout << "Hello world!";
    vector<int> items = {1, 20, 40, 3, 3, 5, 5, 6, 7, 8, 6, 1};
    QuickSort::sort(items);
    for(auto item: items){
        cout<<item<<endl;
    }
    return 0;
}