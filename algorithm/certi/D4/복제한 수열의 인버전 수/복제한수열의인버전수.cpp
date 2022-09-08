#include <iostream>

#define MOD 1000000007

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
	int test_case, T, arr[2000], N;
    unsigned long long K, answer, left[2000], right[2000];

	std::cin >> T;
	for(test_case = 1; test_case <= T; ++test_case) {
        std::cin >> N >> K;
        for (int i = 0; i < N; ++i) std::cin >> arr[i];

        for (int i = 0; i < N; ++i) {
            left[i] = right[i] = 0;
            for (int j = i+1; j < N; ++j) {
                if (arr[i] == arr[j]) continue;
                if (arr[i] > arr[j]) ++right[i];
                else ++left[i];
            }
        }
        
        answer = 0;
        for (int i = 0; i < N; ++i) {
            answer += right[i] * K % MOD;
            int tmp = K * (K-1) / 2 % MOD;
            tmp = (left[i] + right[i]) * tmp % MOD;
            answer = (answer + tmp) % MOD;
        }
        std::cout << "#" << test_case << " " << answer << '\n';
	}
	return 0;
}