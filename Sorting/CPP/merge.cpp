// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>
class MergeSort{
    private:
        static void merge(std::vector<int> &arr, int lo, int mid, int hi){
            std::vector<int> leftSorted, rightSorted;
            for(int i=lo; i <= mid; i++){
                leftSorted.push_back(arr[i]);
                int j = (i - lo) + mid + 1;
                rightSorted.push_back(arr[j]);
            }
            int leftIdx = 0, rightIdx = 0;
            int k = lo;
            while (leftIdx < leftSorted.size() && rightIdx < rightSorted.size()){
                if (leftSorted[leftIdx] < rightSorted[rightIdx]){
                    arr[k++] = leftSorted[leftIdx++];
                } else{
                    arr[k++] = rightSorted[rightIdx++];
                }
            }
            
            while (leftIdx < leftSorted.size()){
                arr[k++] = leftSorted[leftIdx++];
            }
            while (rightIdx < rightSorted.size()){
                arr[k++] = rightSorted[rightIdx++];
            }
        }
        
        static void sort(std::vector<int> &arr, int lo, int hi){
            if (lo >= hi) return;
            int mid = lo + (hi - lo) /2;
            MergeSort::sort(arr, lo, mid);
            MergeSort::sort(arr, mid+1, hi);
            MergeSort::merge(arr, lo, mid, hi);
        }
    public:
        static void sort(std::vector<int> &arr){
            MergeSort::sort(arr, 0, arr.size() - 1);
        }
};
int main() {
    // Write C++ code here
    std::vector<int> arr = {10, 4, 9 , 3 , 2 ,5, 1, 6};
    MergeSort::sort(arr);
    for(auto num: arr){
        std::cout << num << std::endl;
    }
    return 0;
}