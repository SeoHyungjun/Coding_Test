#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, N, M, lost;

    std::cin >> T;
    while (T--) {
        std::cin >> N >> M;
        lost = M + M - N;
        std::cout << lost << ' ' << M - lost << '\n';
    }

    return 0;
}