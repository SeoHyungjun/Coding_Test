#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, cnt = 0;

    std::cin >> N;
    while (N) {
        if (N & 1) ++cnt;
        if (cnt > 1) break;
        N >>= 1;
    }

    std::cout << (cnt > 1?0:1);

    return 0;
}