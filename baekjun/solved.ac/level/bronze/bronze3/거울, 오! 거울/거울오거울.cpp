#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;

    while (true) {
        std::getline(std::cin, str);
        if (str == "***") break;
        std::reverse(str.begin(), str.end());
        std::cout << str << "\n";
    }

    return 0;
}
