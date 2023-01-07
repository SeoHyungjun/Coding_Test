#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int N, arr[8];

int cal() {
    int sum = 0;

    for (int i = 1; i < N; ++i) sum += std::abs(arr[i] - arr[i-1]);

    return sum;
}

int dfs(int idx) {
    int result = -1000;

    if (idx >= N ) return cal();

    for (int i = idx; i < N; ++i) {
        std::swap(arr[idx], arr[i]);
        result = std::max(result, dfs(idx + 1));
        std::swap(arr[idx], arr[i]);
    }

    return result;
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);

    std::cin >> N;
    for (int i = 0; i < N; ++i) std::cin >> arr[i];

    std::cout << dfs(0);

    return 0;
}