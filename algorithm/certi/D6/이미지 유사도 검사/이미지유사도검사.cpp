#include <iostream>

int test_case, T, N, dp[502][502];
std::string A, B;

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::cout << std::fixed;
    std::cout.precision(2);

	std::cin >> T;
	for(test_case = 1; test_case <= T; ++test_case) {
        std::cin >> N >> A >> B;

        for (int i = 0; i <= N; ++i) {dp[0][i] = 0;dp[i][0] = 0;}
        for (int i = 1; i <= N; ++i) for (int j = 1; j <= N; ++j) dp[i][j] = (A[i-1] == B[j-1]) ? dp[i-1][j-1] + 1 : std::max(dp[i-1][j], dp[i][j-1]);

        std::cout << "#" << test_case << ' ' << (double)dp[N][N] / N * 100 << '\n';
	}
	return 0;
}