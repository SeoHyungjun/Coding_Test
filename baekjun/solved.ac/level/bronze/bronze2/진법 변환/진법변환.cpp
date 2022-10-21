#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;
    int N, answer = 0;

    std::cin >> str >> N;
    for (int i = 0; i < str.length(); ++i) {
        if (str[i] >= '0' && str[i] <= '9') answer = answer * N + str[i] - '0';
        else answer = answer * N + str[i] - 'A' + 10;
    }

    std::cout << answer;

    return 0;
}