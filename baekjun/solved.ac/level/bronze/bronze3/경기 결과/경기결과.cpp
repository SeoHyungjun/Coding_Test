#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, a, b, A = 0, B = 0;

    std::cin >> N;
    while (N--) {
        std::cin >> a >> b;
        if (a > b) ++A;
        else if (a < b) ++B;
    }

    std::cout << A << ' ' << B;

    return 0;
}