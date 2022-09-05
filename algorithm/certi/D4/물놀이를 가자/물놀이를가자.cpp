#include <iostream>
#include <string>
#include <deque>

std::deque<std::pair<int, int>> q;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int board[1001][1001] = {0, };

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
	int test_case, T, answer;
    int N, M, i, j, k, next_i, next_j;
    std::string str, print_answer = "";

	std::cin >> T;
	for(test_case = 1; test_case <= T; ++test_case) {
        answer = 0;
        std::cin >> N >> M;
        for (i = 0; i < N; ++i) {
            std::cin >> str;
            for (int j = 0; j < M; ++j) {
                if (str[j] == 'L') {
                    board[i][j] = 2000;
                    answer += 2000;
                    continue;
                }
                q.emplace_back(i, j);
                board[i][j] = 0;
            }
        }

        while (!q.empty()) {
            auto cur = q.front();
            i = cur.first, j = cur.second;
            q.pop_front();

            for (k = 0; k < 4; ++k) {
                next_i = i + dx[k];
                next_j = j + dy[k];

                if (next_i < 0 || next_i >= N || next_j < 0 || next_j >= M) continue;
                if (board[next_i][next_j] <= board[i][j] + 1) continue;
                answer -= board[next_i][next_j] - board[i][j] - 1;
                board[next_i][next_j] = board[i][j] + 1;
                q.emplace_back(next_i, next_j);
            }
        }

        print_answer += "#" + std::to_string(test_case) + ' ' + std::to_string(answer) + '\n';
	}
    std::cout << print_answer;
	return 0;
}