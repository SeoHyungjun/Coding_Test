#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

double price[5] = {350.34, 230.90, 190.55, 125.30, 180.90};

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::cout << std::fixed; std::cout.precision(2);
    int T, p;
    double answer;

    std::cin >> T;
    while (T--) {
        answer = 0.0;

        for (int i = 0; i < 5; ++i) {
            std::cin >> p;
            answer += p * price[i];
        }
        std::cout << '$' << answer << '\n';
    }

    return 0;
}