#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, d, n, s, p, serial, parallel;

    std::cin >> T;
    while (T--) {
        std::cin >> d >> n >> s >> p;
        serial = n * s;
        parallel = n * p + d;

        if (serial > parallel) std::cout << "parallelize\n";
        else if (serial < parallel) std::cout << "do not parallelize\n";
        else std::cout << "does not matter\n";
    }

    return 0;
}