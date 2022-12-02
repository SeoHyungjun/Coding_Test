#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;
    int answer = 10;

    std::cin >> str;
    for (int i = 1; i < str.length(); ++i) {
        if (str[i] == str[i-1]) answer += 5;
        else answer += 10;
    }

    std::cout << answer;

    return 0;
}