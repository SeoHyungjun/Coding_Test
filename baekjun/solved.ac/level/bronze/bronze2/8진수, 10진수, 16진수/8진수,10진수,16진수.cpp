#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;
    int answer = 0;

    std::cin >> str;
    if (str.length() >= 2 && str[0] == '0' && str[1] == 'x') {
        int tmp = 1;
        for (int i = str.length() - 1; i >= 2; --i) {
            if (str[i] >= '0' && str[i] <= '9') answer += tmp * (str[i] - '0');
            else answer += tmp * (str[i] - 'a' + 10);
            tmp *= 16;
        }
        std::cout << answer;
    }
    else if (str[0] == '0') {
        int tmp = 1;
        for (int i = str.length() - 1; i >= 1; --i) {
            answer += tmp * (str[i] - '0');
            tmp *= 8;
        }
        std::cout << answer;
    }
    else std::cout << str;

    return 0;
}