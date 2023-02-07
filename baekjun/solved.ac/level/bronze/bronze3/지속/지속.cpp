#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, tmp, answer = 0;

    std::cin >> N;
    while (N >= 10) {
        tmp = 1;

        while (N) {
            tmp *= N % 10;
            N /= 10;
        }

        N = tmp;
        ++answer;
    }

    std::cout << answer;

    return 0;
}