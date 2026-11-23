#include <iostream>
#include <vector>
#include <utility> // для std::swap

void bubbleSort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        bool swapped = false;

        // Последние i элементов уже на своих местах
        for (int j = 0; j < n - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }

        // Если перестановок не было, массив уже отсортирован
        if (!swapped) {
            break;
        }
    }
}

