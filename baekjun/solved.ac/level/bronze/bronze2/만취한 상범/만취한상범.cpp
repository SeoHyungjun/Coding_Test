#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, N, answer;
    bool jail[101]; // false : close, true : open

    std::cin >> T;
    while (T--) {
        std::cin >> N;

        for (int i = 1; i <= N; ++i) jail[i] = true;
        for (int i = 2; i <= N; ++i) {
            for (int j = i; j <= N; j += i) {
                jail[j] = !jail[j];
            }
        }

        answer = 0;
        for (int i = 1; i <= N; ++i) {
            if (jail[i]) ++answer;
        }
        std::cout << answer << '\n';
    }

    return 0;
}