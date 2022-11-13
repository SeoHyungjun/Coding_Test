#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, n, m, answer;

    std::cin >> T;
    while (T--) {
        std::cin >> n >> m;
        answer = 0;

        for (int a = 1; a < n; ++a) {
            for (int b = a + 1; b < n; ++b) {
                if ((a*a + b*b + m) % (a*b) == 0) ++answer;
            }
        }

        std::cout << answer << '\n';
    }

    return 0;
}