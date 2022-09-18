#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T;
    std::string str, tmp;

    std::cin >> T;
    std::cin.ignore();
    while (T--) {
        std::getline(std::cin, str);

        tmp = "";
        for (int i = 0; i <= str.length(); ++i) {
            if (str[i] == ' ' or i == str.length()) {
                std::reverse(tmp.begin(), tmp.end());
                std::cout << tmp << ' ';
                tmp = "";
                continue;
            }
            tmp += str[i];
        }
        std::cout << '\n';
    }
    return 0;
}