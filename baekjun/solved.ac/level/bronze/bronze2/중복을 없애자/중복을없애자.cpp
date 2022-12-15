#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, cur, prev;

    while (true) {
        std::cin >> N;
        if (!N) break;

        prev = 0;
        while (N--) {
            std::cin >> cur;
            if (cur == prev) continue;
            std::cout << cur << ' ';
            prev = cur;
        }
        std::cout << "$\n";
    }
    return 0;
}