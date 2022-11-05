#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, mul, answer;
    char str[25];

    std::cin >> N;
    std::cin.ignore();
    while (N--) {
        std::cin >> str;

        mul = 1;
        answer = 0;
        for (int i = 23; i >= 0; --i) {
            answer += mul * (str[i] - '0');
            mul *= 2;
        }
        std::cout << answer << '\n';
    }

    return 0;
}