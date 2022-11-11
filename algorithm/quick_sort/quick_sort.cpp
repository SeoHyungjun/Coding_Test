#include <iostream>

#define MAX_NUM 10

int arr[MAX_NUM] = {1, 3, 10, 5, 8, 9, 2, 4, 6, 7};

void quick_sort(int first, int last) {
    int pivot, i, j, tmp;

    if (first >= last) return;
    pivot = first;
    i = first + 1;
    j = last;

    while (i < j) {
        while (arr[i] <= arr[pivot] && i < last) ++i;
        while (arr[j] > arr[pivot]) --j;
        if (i < j) {
            tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
    }
    tmp = arr[pivot];
    arr[pivot] = arr[j];
    arr[j] = tmp;

    quick_sort(first, j - 1);
    quick_sort(j + 1, last);
}

void print_result() {
    int i;
    for (i = 0; i < MAX_NUM; ++i) std::cout << arr[i] << ' ';
    std::cout << '\n';
}

int main() {
    print_result();
    quick_sort(0, 9);
    print_result();

    return 0;
}

/*
void quick_sort(int first, int last) {
    int pivot, i, j, tmp;

    if (first >= last) return;
    pivot = first;
    i = first;
    j = last;
    
    while (i < j) {
        while (arr[i] <= arr[pivot] && i < last) ++i;
        while (arr[j] > arr[pivot]) --j;
        if (i < j) {
            tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
    }
    tmp = arr[pivot];
    arr[pivot] = arr[j];
    arr[j] = tmp;

    quick_sort(first, j - 1);
    quick_sort(j + 1, last);
}

*/