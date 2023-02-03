#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, a, b;

    std::cin >> T;
    for (int i = 1; i <= T; ++i) {
        std::cin >> a >> b;
        std::cout << "Case " << i << ": " << a + b << '\n';
    }

    return 0;
}