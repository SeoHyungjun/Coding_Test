#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, row;
    std::string str;

    std::cin >> T;
    while (T--) {
        std::cin >> str;

        row = sqrt(str.length());
        for (int j = row - 1; j >= 0; --j) {
            for (int i = 0; i < row; ++i) {
                std::cout << str[i * row + j];
            }
        }
        std::cout << '\n';
    }

    return 0;
}