#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, N, C, total_C;
    float G, total_G;

    std::cin >> T;
    while (T--) {
        total_C = 0;
        total_G = 0.0;

        std::cin >> N;
        while (N--) {
            std::cin >> C >> G;
            total_C += C;
            total_G += G * C;
        }

        std::cout << total_C << ' ' << total_G / total_C << '\n';
    }

    return 0;
}