#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int N, arr[10001];

bool next_permutation() {
    int left = N - 1;
    while (left > 0 && arr[left - 1] > arr[left]) --left;

    if (!left) return false;

    int right = N - 1;
    while (arr[left - 1] > arr[right]) --right;
    std::swap(arr[left - 1], arr[right]);
    std::sort(arr + left, arr + N);

    return true;
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);

    std::cin >> N;
    for (int i = 0; i < N; ++i) std::cin >> arr[i];
    
    if (next_permutation()) {
        for (int i = 0; i < N; ++i) std::cout << arr[i] << ' ';
    }
    else std::cout << -1;

    return 0;
}