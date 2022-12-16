#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;
    bool check[26] = {0, };

    while (true) {
        std::getline(std::cin, str);
        if (str == "#") break;
        
        for (int i = 0; i < str.length(); ++i) {
            if (str[i] >= 'a' & str[i] <= 'z') check[str[i] - 'a'] = true;
            else if (str[i] >= 'A' & str[i] <= 'Z') check[str[i] - 'A'] = true;
        }

        int answer = 0;
        for (int i = 0; i < 26; ++i) {
            if (check[i]) ++answer;
            check[i] = 0;
        }

        std::cout << answer << '\n';
    }

    return 0;
}