#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;
    int start;

    while (true) {
        std::cin >> str;
        if (str == "#") break;

        start = 0;
        for (int i = 0; i < str.length(); ++i) {
            if (str[i] != 'a' && str[i] != 'e' && str[i] != 'i' && str[i] != 'o' && str[i] != 'u')
                continue;
            start = i;
            break;
        }

        for (int i = start; i < str.length() + start; ++i) {
            std::cout << str[i % str.length()];
        }
        std::cout << "ay\n";
    }

    return 0;
}