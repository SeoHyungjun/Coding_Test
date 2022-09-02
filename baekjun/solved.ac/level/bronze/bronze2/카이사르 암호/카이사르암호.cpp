#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;

    std::cin >> str;
    for (int i = 0; i < str.length(); ++i) {
        std::cout << char((str[i] - 'A' - 3 + 26) % 26 + 'A');
    }

    return 0;
}