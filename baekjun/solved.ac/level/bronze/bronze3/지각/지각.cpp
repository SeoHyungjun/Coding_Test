#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, N, answer;

    std::cin >> T;
    while (T--) {
        std::cin >> N;
        answer = sqrt(N);
        if (answer*answer + answer > N) answer -= 1;
        std::cout << answer << '\n';
    }

    return 0;
}