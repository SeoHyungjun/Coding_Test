#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;
    int answer_joi = 0, answer_ioi = 0;

    std::cin >> str;
    for (int i = 0; i < str.length() - 2; ++i) {
        if (str[i] == 'J' && str[i+1] == 'O' && str[i+2] == 'I') ++answer_joi;
        if (str[i] == 'I' && str[i+1] == 'O' && str[i+2] == 'I') ++answer_ioi;
    }

    std::cout << answer_joi << '\n' << answer_ioi;

    return 0;
}