#include <iostream>
#include <string>

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);

	int test_case, N, i, j, k, answer;
    std::string board[8], print_answer = "";
    bool is_palindrome;

	for(test_case = 1; test_case <= 10; ++test_case) {
        answer = 0;

        std::cin >> N;
        for (i = 0; i < 8; i++) std::cin >> board[i];
        for (i = 0; i < 8; i++) {
            for (j = 0; j < 8 - N + 1; j++) {
                // row
                is_palindrome = true;
                for (k = 0; k + k <= N; k++) {
                    if (board[i][j + k] == board[i][j + N - 1 - k]) continue;
                    is_palindrome = false;
                    break;
                }
                if (is_palindrome) answer += 1;

                // column
                is_palindrome = true;
                for (k = 0; k + k <= N; k++) {
                    if (board[j + k][i] == board[j + N - 1 - k][i]) continue;
                    is_palindrome = false;
                    break;
                }
                if (is_palindrome) answer += 1;
            }
        }
        print_answer += '#' + std::to_string(test_case) + ' ' + std::to_string(answer) + '\n';
	}
    std::cout << print_answer;

	return 0;
}