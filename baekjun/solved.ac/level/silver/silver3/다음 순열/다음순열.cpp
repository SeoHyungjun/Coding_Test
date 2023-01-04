#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, arr[10001];

    std::cin >> N;
    for (int i = 0; i < N; ++i) std::cin >> arr[i];

    if (std::next_permutation(arr, arr + N)) {
        for (int i = 0; i < N; ++i) std::cout << arr[i] << ' ';
    }
    else std::cout << -1;
}