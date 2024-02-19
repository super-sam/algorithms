#include <iostream>
#include <vector>

using namespace std;

class Selection{
    public:
    static void sort(std::vector<int> &items){
        for (int i = 0; i < items.size() - 1; i++){
            int min_index = i;
            for (int j = i+1; j < items.size(); j++){
                if (Selection::less(items[j], items[min_index])) {
                    min_index = j;
                }
            }
            Selection::exch(items, i, min_index);
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
    Selection::sort(arr);
    for(auto item : arr){
		cout << item << " ";
    }
    return 0;
}