#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

void swap(int* arr, int a, int b) {
    int tmp = arr[a];
    arr[a] = arr[b];
    arr[b] = tmp;

    for (int i = 0; i < 5; ++i) std::cout << arr[i] << ' ';
    std::cout << '\n';
}

void change(int* arr) {
    if (arr[0] > arr[1]) swap(arr, 0, 1);
    if (arr[1] > arr[2]) swap(arr, 1, 2);
    if (arr[2] > arr[3]) swap(arr, 2, 3);
    if (arr[3] > arr[4]) swap(arr, 3, 4);
}

bool check(int* arr) {
    for (int i = 0; i < 5; ++i) if (arr[i] != i + 1) return false;
    return true;
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int arr[5];

    for (int i = 0; i < 5; ++i) std::cin >> arr[i];

    while (!check(arr)) {
        change(arr);
    }

    return 0;
}