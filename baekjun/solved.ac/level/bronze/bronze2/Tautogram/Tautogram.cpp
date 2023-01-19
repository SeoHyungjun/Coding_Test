#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;
    bool flag;
    char c;

    while (true) {
        std::getline(std::cin, str);
        if (str == "*") break;

        std::transform(str.begin(), str.end(), str.begin(), ::tolower);
        c = str[0];
        flag = true;
        for (int i = 1; i < str.length(); ++i) {
            if (str[i - 1] == ' ' && str[i] != c) {
                flag = false;
                break;
            }
        }
        std::cout << (flag ? "Y\n" : "N\n");
    }

    return 0;
}