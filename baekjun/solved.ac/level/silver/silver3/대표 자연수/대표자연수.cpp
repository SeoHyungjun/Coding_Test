#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int N, arr[20001];

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);

    std::cin >> N;
    for (int i = 0; i < N; ++i) std::cin >> arr[i];
    std::sort(arr, arr+N);

    std::cout << arr[(N - 1) / 2];

    return 0;
}