#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;
    int answer = 0, tmp = 0;

    while (std::getline(std::cin, str)) {
        for (int i = 0; i < str.length(); ++i) {
            if (str[i] == ',') {
                answer += tmp;
                tmp = 0;
                continue;
            }
            tmp = tmp * 10 + str[i] - '0';
        }
    }
    answer += tmp;
    std::cout << answer;

    return 0;
}
