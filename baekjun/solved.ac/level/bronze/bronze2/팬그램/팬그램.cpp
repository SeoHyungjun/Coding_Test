#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <cstring>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;
    bool alpha[26], check;

    while (true) {
        memset(alpha, 0, sizeof(false)*26);
        getline(std::cin, str);
        if (str == "*") break;

        for (char c : str) if (c != ' ') alpha[c - 'a'] = true;

        check = true;
        for (bool cur : alpha) {
            if (cur) continue;
            check = false;
            break;
        }
        std::cout << (check ? "Y\n" : "N\n");
    }
    return 0;
}