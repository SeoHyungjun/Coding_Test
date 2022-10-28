#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, M, arr[500000], cur;

    std::cin >> N;
    for (int i = 0; i < N; ++i) std::cin >> arr[i];
    std::sort(arr, arr + N);
    std::cin >> M;
    while (M--) {
        std::cin >> cur;
        if (arr[std::lower_bound(arr, arr + N, cur) - arr] == cur) std::cout << "1 ";
        else std::cout << "0 ";
    }

    return 0;
}