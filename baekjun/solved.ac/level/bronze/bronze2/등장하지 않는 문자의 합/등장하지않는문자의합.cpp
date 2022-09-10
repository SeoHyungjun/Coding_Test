#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;
    int N, answer;
    bool alpha[26] = {false, };

    std::cin >> N;
    while (N--) {
        std::cin >> str;
        for (int i = 0; i < str.length(); ++i) alpha[str[i] - 65] = true;

        answer = 0;
        for (int i = 0; i < 26; ++i) {
            if (!alpha[i]) answer += i + 65;
            else alpha[i] = false;
        }

        std::cout << answer << '\n';
    }
    return 0;
}