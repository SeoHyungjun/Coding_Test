#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, n;

    std::cin >> T;
    while (T--) {
        bool first = true;
        std::cin >> n;
        std::cout << "Pairs for " << n << ": ";
        for (int i = 1; i < 6; ++i) {
            if (n - i <= i) continue;
            if (first) first = false;
            else std::cout << ", ";
            std::cout << i << ' ' << n - i;
        }
        std::cout << '\n';
    }
    return 0;
}