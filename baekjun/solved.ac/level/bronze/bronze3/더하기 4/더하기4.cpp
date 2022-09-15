#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, answer;
    std::string str, tmp;

    std::cin >> T;
    std::cin.ignore();
    while (T--) {
        getline(std::cin, str);
        answer = 0;
        tmp = "";
        for (int i = 0; i < str.length(); ++i) {
            if (str[i] == ' ') {
                answer += std::stoi(tmp);
                tmp = "";
                continue;
            }
            tmp += str[i];
        }
        answer += std::stoi(tmp);
        std::cout << answer << '\n';
    }
    return 0;
}