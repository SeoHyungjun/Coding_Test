#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

using ll = long long;
#define MOD 1000000000;

int N;
ll dp[100][10], answer = 0;

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);

    std::cin >> N;

    dp[0][0] = 0;
    for (int i = 1; i < 10; ++i) dp[0][i] = 1;

    for (int i = 1; i < N; ++i) {
        for (int j = 0; j < 10; ++j) {
            if (j == 0) dp[i][j] = dp[i - 1][j + 1];
            else if (j == 9) dp[i][j] = dp[i - 1][j - 1];
            else dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD;
        }
    }

    for (int i = 0; i < 10; ++i) answer += dp[N-1][i];
    std::cout << answer % MOD;

    return 0;
}