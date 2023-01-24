#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int A, B, C;

    while (std::cin >> A >> B >> C) {
        std::cout << std::max(B - A, C - B) - 1 << '\n';
    }

    return 0;
}