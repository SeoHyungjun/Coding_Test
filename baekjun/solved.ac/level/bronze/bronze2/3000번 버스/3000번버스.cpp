#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, K, answer;

    std::cin >> T;
    while (T--) {
        std::cin >> K;
        answer = 0;
        while (K--) answer = 2 * answer + 1;
        std::cout << answer << '\n';
    }

    return 0;
}