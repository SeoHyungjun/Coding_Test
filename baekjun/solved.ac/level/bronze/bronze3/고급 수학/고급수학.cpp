#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, a, b, c;

    std::cin >> N;

    for (int i = 1; i <= N; ++i) {
        std::cin >> a >> b >> c;
        a *= a; b *= b; c *= c;
        
        if (i != 1) std::cout << '\n';
        std::cout << "Scenario #" << i << ":\n";
        if (a == b + c || b == a + c || c == a + b) std::cout << "yes\n";
        else std::cout << "no\n";
    }

    return 0;
}