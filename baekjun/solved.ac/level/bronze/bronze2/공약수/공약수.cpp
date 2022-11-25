#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, a, b, c = 0;

    std::cin >> N;

    if (N == 2) std::cin >> a >> b;
    else std::cin >> a >> b >> c;

    for (int i = 1; i <= std::min(a, b); ++i) {
        if (a % i == 0 && b % i == 0 && c % i == 0)
            std::cout << i << '\n';
    }

    return 0;
}