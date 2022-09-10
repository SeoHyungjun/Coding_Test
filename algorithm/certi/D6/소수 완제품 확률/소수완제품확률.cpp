#include <iostream>

int prime[7] = {2, 3, 5, 7, 11, 13, 17};
int combination[19][19];

void init_combination() { // nCr을 위해 comb[n][r]을 미리 계산
    for (int i = 0; i < 19; ++i) {
        combination[i][0] = 1;
        combination[i][i] = 1;
    }
    for (int i = 2; i < 19; ++i) {
        for (int j = 1; j <= i; ++j) combination[i][j] = combination[i-1][j-1] + combination[i-1][j];
    }
}

double calculate(int percent, int s) {
    double result = 1.0, p = (double)percent / 100;
    while (s--) result *= p;
    return result;
}

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::cout << std::fixed;
    std::cout.precision(6);
	int test_case, T, A, B;
    double answer_A, answer_B, answer = 0.0;

	//freopen("input.txt", "r", stdin);
	std::cin >> T;
    init_combination();
	for(test_case = 1; test_case <= T; ++test_case) {
        std::cin >> A >> B;
        answer_A = 0.0; answer_B = 0.0;
        for (int i = 0; i < 7; ++i) {
            double success_A = calculate(A, prime[i]); // A가 prime 수 만큼 완제품 생성
            double success_B = calculate(B, prime[i]); // B가 prime 수 만큼 완제품 생성
            double failure_A = calculate(100 - A, 18 - prime[i]); // 18개 - 완제품 수 = 실패 수
            double failure_B = calculate(100 - B, 18 - prime[i]); // 18개 - 완제품 수 = 실패 수

            answer_A += combination[18][prime[i]] * success_A * failure_A; // 18개중 prime 수 만큼 생산하는 확률 * 성공확률 * 실패확률
            answer_B += combination[18][prime[i]] * success_B * failure_B;
        }
        answer = 1 - ((1 - answer_A) * (1 - answer_B));
        std::cout << "#" << test_case << " " << answer << '\n';
	}
	return 0;
}