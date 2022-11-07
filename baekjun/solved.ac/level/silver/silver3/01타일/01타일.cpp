#include <iostream>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, dp[3] = {0, 1, 2};

    std::cin >> N;
    for (int i = 3; i <= N; ++i) dp[i % 3] = (dp[(i-1) % 3] + dp[(i-2) % 3]) % 15746;

    std::cout << dp[N % 3];

    return 0;
}