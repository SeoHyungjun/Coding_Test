#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, T, cur, sum = 0;

    std::cin >> N >> T;
    for (int i = 0; i < N; ++i) {
        std::cin >> cur;
        sum += cur;

        if (sum > T) {
            std::cout << i;
            break;
        }
    }

    if (sum <= T) std::cout << N;

    return 0;
}