#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int M, N, min_prime = 10001, sum = 0;
bool is_not_prime[10001] = {false, };

void check_prime() {
    for (int i = 2; i < sqrt(N) + 1; ++i) {
        if (is_not_prime[i]) continue;
        for (int j = i + i; j <= N; j += i) is_not_prime[j] = true;
    }
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);

    std::cin >> M;
    std::cin >> N;

    is_not_prime[0] = is_not_prime[1] = true;
    check_prime();

    for (int i = M; i <= N; ++i) {
        if (is_not_prime[i]) continue;
        sum += i;
        min_prime = std::min(min_prime, i);
    }

    if (sum > 0) std::cout << sum << '\n' << min_prime;
    else std::cout << "-1";

    return 0;
}