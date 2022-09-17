#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, N, C;

    std::cin >> T;
    while (T--) {
        std::cin >> N >> C;
        std::cout << (int)ceil((double)N/C) << '\n';
    }

    return 0;
}