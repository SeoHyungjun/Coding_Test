#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <cstring>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str1, str2;
    int alpha1[26], alpha2[26];
    bool flag;

    for (int t = 1; ; ++t) {
        std::cin >> str1 >> str2;
        if (str1 == "END" && str2 == "END") break;
        if (str1.length() != str2.length()) {
            flag = false;
        }
        else {
            memset(alpha1, 0, sizeof(int) * 26);
            memset(alpha2, 0, sizeof(int) * 26);
            for (int i = 0; i < str1.length(); ++i) {
                ++alpha1[str1[i] - 'a'];
                ++alpha2[str2[i] - 'a'];
            }

            flag = true;
            for (int i = 0; i < 26; ++i) {
                if (alpha1[i] == alpha2[i]) continue;
                flag = false;
                break;
            }
        }
        std::cout << "Case " << t << ": " << (flag ? "same\n" : "different\n");
    }

    return 0;
}