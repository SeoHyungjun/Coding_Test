#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, N, K, cur, answer;

    std::cin >> T;
    while (T--) {
        std::cin >> N >> K;

        answer = 0;
        while (N--) {
            std::cin >> cur;
            answer += cur/K;
        }
        std::cout << answer << '\n';
    }

    return 0;
}