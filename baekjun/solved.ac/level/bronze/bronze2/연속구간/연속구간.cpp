#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, prev, cnt, tmp, answer;

    for (int i = 0; i < 3; ++i) {
        std::cin >> N;

        cnt = 0;
        prev = -1;
        answer = 1;
        while (N) {
            tmp = N % 10;
            if (tmp == prev) ++cnt;
            else {
                prev = tmp;
                cnt = 1;
            }
            N /= 10;
            answer = std::max(answer, cnt);
        }
        std::cout << answer << '\n';
    }
    return 0;
}