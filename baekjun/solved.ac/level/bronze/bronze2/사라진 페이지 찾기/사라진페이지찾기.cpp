#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, P;

    while (true) {
        std::cin >> N;
        if (!N) break;
        std::cin >> P;

        if (P <= N / 2) {
            if (P & 1) std::cout << P + 1 << ' ' << N - P << ' ' << N - P + 1 << '\n';
            else std::cout << P - 1 << ' ' << N - P + 1 << ' ' << N - P + 2 << '\n';
        }
        else {
            if (P & 1) std::cout << N - P << ' ' << N - P + 1 << ' ' << P + 1 << '\n';
            else std::cout << N - P + 1 << ' ' << N - P + 2 << ' ' << P - 1 << '\n';
        }
    }

    return 0;
}