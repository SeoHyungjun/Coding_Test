#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, A, B;

    std::cin >> T;
    while (T--) {
        std::cin >> A >> B;
        std::cout << (A/B)*(A/B) << '\n';
    }

    return 0;
}