#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str[5];
    int index[5] = {0, };

    for (int i = 0; i < 5; ++i) std::cin >> str[i];

    for (int t = 0; t < 15; ++t) {
        for (int i = 0; i < 5; ++i) {
            if (str[i][index[i]] == '\0') continue;
            std::cout << str[i][index[i]++];
        }
    }

    return 0;
}