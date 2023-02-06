#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, N, num, min, max;

    std::cin >> T;
    while (T--) {
        std::cin >> N;
        min = 1000001;
        max = -1000001;
        while (N--) {
            std::cin >> num;
            if (num < min) min = num;
            if (num > max) max = num;
        }
        std::cout << min << ' ' << max << '\n';
    }

    return 0;
}