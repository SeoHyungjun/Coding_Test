#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, B, cur;
    std::string answer;

    std::cin >> N >> B;

    while (N) {
        cur = N % B;
        answer += (cur < 10)?('0' + cur):('A' + (cur - 10));
        N /= B;
    }

    std::reverse(answer.begin(), answer.end());
    std::cout << answer;

    return 0;
}