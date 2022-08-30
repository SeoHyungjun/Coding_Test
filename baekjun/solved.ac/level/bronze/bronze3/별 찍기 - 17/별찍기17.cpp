#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);

    int N = 0;

    std::cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N-1 - i; j++) std::cout << ' ';
        for (int j = 0; j < 2*i + 1; j++) {
            if (i == 0 || i == N-1 || j == 0 || j == 2*i) std::cout << '*';
            else std::cout << ' ';
        }
        std::cout << '\n';
    }

    return 0;
}