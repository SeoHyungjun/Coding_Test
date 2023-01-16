#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

bool not_prime[1001] = {false, };

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, K, cnt = 0;

    std::cin >> N >> K;

    for (int i = 2; i <= N; ++i) {
        for (int j = i; j <= N; j += i) {
            if (not_prime[j]) continue;
            not_prime[j] = true;
            ++cnt;
            if (cnt == K) {
                std::cout << j;
                return 0;
            }
        }
    }

    return 0;
}