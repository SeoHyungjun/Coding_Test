#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;

    while (getline(std::cin, str)) {
        int lower = 0, upper = 0, num = 0, space = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str[i] >= 'a' && str[i] <= 'z') ++lower;
            else if (str[i] >= 'A' && str[i] <= 'Z') ++upper;
            else if (str[i] >= '0' && str[i] <= '9') ++num;
            else if (str[i] == ' ') ++space;
        }
        std::cout << lower << ' ' << upper << ' ' << num << ' ' << space << '\n';
    }

    return 0;
}