#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N;
    std::string str;

    std::cin >> N;
    std::cin.ignore();
    while (N--) {
        std::getline(std::cin, str);
        if (str.substr(0, 10) != "Simon says") continue;
        std::cout << str.substr(10, 100) << '\n';
    }

    return 0;
}