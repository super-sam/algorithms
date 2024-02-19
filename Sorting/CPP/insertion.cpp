#include <iostream>
#include <vector>

using namespace std;

class Insertion{
    public:
    static void sort(std::vector<int> &items){
        const int N = items.size();
        for (int i = 1; i < N; i++){
            for (int j = i; j > 0; j--){
                if (!Insertion::less(items[j], items[j-1])) break;
                Insertion::exch(items, j, j-1);
            }
            
        }
    }
    static bool less(int a, int b){
        return a < b;
    }
    static void exch(std::vector<int> &items, int i, int j){
        int temp = items[i];
        items[i] = items[j];
        items[j] = temp;
    }
};

int main(){
    std::vector<int> arr = {5, 4, 3, 2, 1};
    Insertion::sort(arr);
    for(auto item : arr){
		cout << item << " ";
    }
    return 0;
}