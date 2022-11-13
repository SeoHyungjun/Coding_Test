#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, N, D, v, f, c, answer;

    std::cin >> T;
    while (T--) {
        std::cin >> N >> D;

        answer = 0;
        while (N--) {
            std::cin >> v >> f >> c;
            if (f * v >= D * c) ++answer;
        }

        std::cout << answer << '\n';
    }

    return 0;
}