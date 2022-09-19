#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;
    int cnt_one, len;

    while (true) {
        std::cin >> str;
        if (str == "#") break;

        cnt_one = 0;
        len = str.length() - 1;
        for (int i = 0; i < len; ++i) if (str[i] == '1') ++cnt_one;
        if ((str[len] == 'e' && cnt_one & 1) or (str[len] == 'o' && !(cnt_one & 1))) str[len] = '1';
        else str[len] = '0';

        std::cout << str + '\n';
    }

    return 0;
}