#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int answer;
    std::string str;

    while (true) {
        std::getline(std::cin, str);
        if (str == "#") break;

        answer = 0;
        for (int i = 0; i < str.length(); ++i) answer += str[i] == ' ' ? 0 : (i+1) * (str[i] - 'A' + 1);

        std::cout << answer << "\n";
    }

    return 0;
}