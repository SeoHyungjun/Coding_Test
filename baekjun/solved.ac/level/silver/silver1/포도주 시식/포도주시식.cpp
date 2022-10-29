#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, arr[10002], dp[10002];

    std::cin >> N;
    for (int i = 1; i <= N; ++i) std::cin >> arr[i];
    dp[1] = arr[1];
    dp[2] = dp[1] + arr[2];
    for (int i = 3; i <= N; ++i) dp[i] = std::max(dp[i-3] + arr[i-1] + arr[i], std::max(dp[i-2] + arr[i], dp[i-1]));

    std::cout << dp[N];

    return 0;
}