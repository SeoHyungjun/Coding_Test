#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N;

    std::cin >> N;
    for (int i = 0; i < N; ++i) {
        for (int j = N - i - 2; j >= 0; --j) std::cout << ' ';
        std::cout << '*';
        for (int j = 0; j < 2 * i - 1; ++j) std::cout << ' ';
        if (i != 0) std::cout << '*';
        std::cout << '\n';
    }

    return 0;
}