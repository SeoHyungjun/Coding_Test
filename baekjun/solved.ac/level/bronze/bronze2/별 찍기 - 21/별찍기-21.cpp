#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N;

    std::cin >> N;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (j % 2) std::cout << " ";
            else std::cout << "*";
        }
        std::cout << "\n";
        for (int j = 0; j < N; ++j) {
            if (j % 2) std::cout << "*";
            else std::cout << " ";
        }
        std::cout << "\n";
    }

    return 0;
}