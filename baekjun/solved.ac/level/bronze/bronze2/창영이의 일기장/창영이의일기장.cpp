#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str, answer = "";

    getline(std::cin, str);
    for (int i = 0; i < str.length(); ++i) {
        if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u') {
            if (i+2 >= str.length() || str[i+1] != 'p' || str[i] != str[i+2]) continue;
            answer += str[i];
            i += 2;
            continue;
        }
        answer += str[i];
    }
    std::cout << answer;

    return 0;
}
