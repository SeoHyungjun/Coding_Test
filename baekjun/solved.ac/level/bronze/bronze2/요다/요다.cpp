#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str, first, second;
    int N, cnt;

    std::cin >> N;
    std::cin.ignore();
    while (N--) {
        std::getline(std::cin, str);
        cnt = 0;
        first = " ";
        second = "";
        for (int i = 0; i < str.length(); ++i) {
            if (cnt < 2) first += str[i];
            else second += str[i];
            if (str[i] == ' ') ++cnt;
        }
        std::cout << second << first << "\n";
    }

    return 0;
}