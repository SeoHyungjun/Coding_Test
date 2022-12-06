#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

std::string deleted_set[10] = {"i", "pa", "te", "ni", "niti", "a", "ali", "nego", "no", "ili"};

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str, tmp, answer = "";

    std::getline(std::cin, str);
    for (int i = 0; i <= str.length(); ++i) {
        if (str[i] != ' ' && i != str.length()) tmp += str[i];
        else {
            bool flag = true;
            for (int j = 0; j < 10; ++j) {
                if (tmp != deleted_set[j]) continue;
                flag = false;
                break;
            }
            if (flag or answer == "") {
                answer += tmp[0];
            }
            tmp = "";
        }
    }

    std::transform(answer.begin(), answer.end(), answer.begin(), ::toupper);
    std::cout << answer;

    return 0;
}