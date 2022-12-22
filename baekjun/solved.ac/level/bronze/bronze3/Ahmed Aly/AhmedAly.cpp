#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, num[3], idx;
    std::string str;
    bool plus, answer;

    std::cin >> T;
    std::cin.ignore();
    for (int t = 1; t <= T; ++t) {
        std::getline(std::cin, str);

        num[0] = num[1] = num[2] = idx = 0;
        plus = false;
        for (int i = 0; i < str.length(); ++i) {
            if (str[i] >= '0' && str[i] <= '9') 
                num[idx] =  num[idx] * 10 + str[i] - '0';
            else if (str[i] == '+' || str[i] == '-' || str[i] == '=') {
                if (str[i] == '+') plus = true;
                ++idx;
            }
        }

        answer = false;
        if (plus && (num[0] + num[1] == num[2])) answer = true;
        if (!plus && (num[0] - num[1] == num[2])) answer = true;

        std::cout << "Case " << t << ": " << (answer?"YES\n":"NO\n");
    }

    return 0;
}