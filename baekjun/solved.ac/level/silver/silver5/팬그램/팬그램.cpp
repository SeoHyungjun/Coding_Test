#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;
    int N, alpha[26], answer;
    bool flag;

    std::cin >> N;
    std::cin.ignore();
    for (int t = 1; t <= N; ++t) {
        std::getline(std::cin, str);

        for (int i = 0; i < 26; ++i) alpha[i] = 0;
        for (int i = 0; i < str.size(); ++i) {
            if (std::tolower(str[i]) < 'a' || std::tolower(str[i]) > 'z') continue;
            alpha[std::tolower(str[i]) - 'a'] += 1;
        }

        answer = 0;
        for (int i = 3; i > 0; --i) {
            flag = true;
            for (int j = 0; j < 26; ++j) {
                if (alpha[j] >= i) continue;
                flag = false;
                break;
            }
            if (flag) {
                answer = i;
                break;
            }
        }

        std::cout << "Case " << t << ": ";
        if (answer == 3) std::cout << "Triple pangram!!!\n";
        else if (answer == 2) std::cout << "Double pangram!!\n";
        else if (answer == 1) std::cout << "Pangram!\n";
        else std::cout << "Not a pangram\n";
    }

    return 0;
}