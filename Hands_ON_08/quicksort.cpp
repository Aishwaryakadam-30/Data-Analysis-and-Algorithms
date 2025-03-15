// implementation of quicksort to implement the ith order statistic

#include<bits/stdc++.h>

using namespace std;

int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];  
    int i = low - 1;        
    
    for (int j = low; j < high; ++j) {
        if (arr[j] <= pivot) {
            ++i;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return (i + 1);
}

int quickSelect(vector<int>& arr, int low, int high, int k) {
    if (low == high) return arr[low];  
    
    int pivotIndex = partition(arr, low, high);
    
    if (pivotIndex == k) {
        return arr[pivotIndex];
    } else if (pivotIndex > k) {
        return quickSelect(arr, low, pivotIndex - 1, k);
    } else {
        return quickSelect(arr, pivotIndex + 1, high, k);
    }
}

int ithOrderStatistic(vector<int>& arr, int i) {
    if(i > arr.size() || i <= 0) return 0;
    return quickSelect(arr, 0, arr.size() - 1, i - 1); 
}

int main() {
    vector<int> arr = {7, 10, 4, 3, 20, 15};
    int i = 1; 
    cout << "The " << i << " smallest element is: " << ithOrderStatistic(arr, i) << endl;
    return 0;
}