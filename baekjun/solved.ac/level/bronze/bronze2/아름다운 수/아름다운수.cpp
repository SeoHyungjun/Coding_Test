#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, X;

    std::cin >> T ;
    while (T--) {
        int point[10] = {0, };
        std::cin >> X;

        while (X) {
            ++point[X%10];
            X /= 10;
        }

        int answer = 0;
        for (int i = 0; i < 10; ++i) {
            if (point[i] == 0) continue;
            ++answer;
        }

        std::cout << answer << '\n';
    }

    return 0;
}