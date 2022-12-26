#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, answer;

    while (true) {
        std::cin >> N;
        if (N == 0) break;
        if (N == 1) {
            std::cout << 1 << '\n';
            continue;
        }
        
        answer = N * N + 1;
        for (int i = 2; i < N; ++i) answer += i * i;

        std::cout << answer << '\n';
    }

    return 0;
}