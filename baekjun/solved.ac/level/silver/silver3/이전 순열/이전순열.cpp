#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int N, arr[10001];

bool prev_permutation() {
    int left = N - 1;
    while (left > 0 & arr[left - 1] < arr[left]) --left;

    if (!left) return false;

    int right = N - 1;
    while (arr[right] > arr[left - 1]) --right;
    std::swap(arr[left - 1], arr[right]);
    std::sort(arr + left, arr + N, std::greater<int>());

    return true;
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);

    std::cin >> N;
    for (int i = 0; i < N; ++i) std::cin >> arr[i];

    if (prev_permutation()) {
        for (int i = 0; i < N; ++i) std::cout << arr[i] << ' ';
    }
    else std::cout << -1;

    return 0;
}