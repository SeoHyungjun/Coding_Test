#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, cur, answer = 0, cnt;

    std::cin >> N;
    for (int student = 1; student < N+1; ++student) {
        cnt = 0;
        for (int i = 0; i < 10; ++i) {
            std::cin >> cur;
            if ((cur - 1) % 5 == i % 5) ++cnt;
        }
        if (cnt == 10) std::cout << student << '\n';
    }
    return 0;
}