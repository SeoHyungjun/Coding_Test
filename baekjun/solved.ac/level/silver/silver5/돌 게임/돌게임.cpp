#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N;
    bool dp[1001] = {false, }; // true : SK, false : CY

    std::cin >> N;

    dp[1] = dp[3] = true;
    for (int i = 4; i <= N; ++i) dp[i] = !(dp[i - 1] | dp[i - 3]);    

    std::cout << (dp[N] ? "SK" : "CY");

    return 0;
}