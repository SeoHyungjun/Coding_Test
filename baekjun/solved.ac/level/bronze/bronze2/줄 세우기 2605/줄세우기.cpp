#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, cur;
    std::vector<int> arr;

    std::cin >> N;
    for (int i = 0; i < N; ++i) {
        std::cin >> cur;
        arr.insert(arr.begin() + i - cur, i + 1);
    }

    for (int i = 0; i < N; ++i) std::cout << arr[i] << ' ';

    return 0;
}