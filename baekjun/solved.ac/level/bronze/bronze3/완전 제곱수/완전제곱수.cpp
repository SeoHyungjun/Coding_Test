#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, answer = 0;

    std::cin >> N;
    for (int i = 1; i < N + 1; ++i) {
        if (N % i == 0 and (N / i + i ) % 2 == 0) answer += 1;
    }

    std::cout << answer / 2;

    return 0;
}