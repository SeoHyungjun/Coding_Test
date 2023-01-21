#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, arr[1000001] = {false, };

    std::cin >> N;
    for (int i = 0; i < N; ++i) std::cin >> arr[i];
    std::sort(arr, arr + N, std::greater<>());

    for (int i = 0; i < N; ++i) std::cout << arr[i] << '\n';

    return 0;
}