#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, K, row, col;
    std::string str[101];
    bool reverse_row = false, reverse_col = false;

    std::cin >> N;
    for (int i = 0; i < N; ++i) std::cin >> str[i];
    std::cin >> K;

    if (K == 2) reverse_col = true;
    else if (K == 3) reverse_row = true;

    for (int i = 0; i < N; ++i) {
        row = (reverse_row) ? N - i - 1 : i;
        for (int j = 0; j < N; ++j) {
            col = (reverse_col) ? N - j - 1 : j;
            std::cout << str[row][col];
        }
        std::cout << "\n";
    }

    return 0;
}