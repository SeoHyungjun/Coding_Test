#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int A, B;

    while (true) {
        std::cin >> A >> B;
        if (A == 0 & B == 0) break;

        std::cout << 2 * A - B << '\n';
    }

    return 0;
}