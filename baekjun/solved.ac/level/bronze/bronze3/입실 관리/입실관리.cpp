#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N;
    std::string str;

    std::cin >> N;
    while (N--) {
        std::cin >> str;
        for (int i = 0; i < str.length(); ++i) std::cout << (char)std::tolower(str[i]);
        std::cout << '\n';
    }

    return 0;
}