#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <cstring>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N;
    std::string str;
    bool alpha[26];

    std::cin >> N;
    std::cin.ignore();
    while (N--) {
        memset(alpha, false, sizeof(bool)*26);
        getline(std::cin, str);

        for (auto c : str) {
            if (c >= 'a' && c <= 'z') alpha[c - 'a'] = true;
            else if (c >= 'A' && c <= 'Z') alpha[c - 'A'] = true;
        }

        std::string tmp = "";
        for (int i = 0; i < 26; ++i) if (!alpha[i]) tmp += i + 'a';

        if (tmp.length() == 0) std::cout << "pangram\n";
        else std::cout << "missing " << tmp + '\n';
    }

    return 0;
}
