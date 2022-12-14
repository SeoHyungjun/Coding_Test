#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int L, P, V, t = 0;

    while (++t) {
        std::cin >> L >> P >> V;
        if (!L & !P & !V) break;

        std::cout << "Case " << t << ": " << (V / P) * L + std::min(V % P, L) << '\n';
    }

    return 0;
}