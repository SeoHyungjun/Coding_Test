#include <iostream>
#include <algorithm>
#include <vector>

int test_case, T, N, board[101][101], dp[21][21], cnt_sub, answer;
bool visit[101][101];
std::vector<std::pair<int, int>> sub_matrix;

void chain_matrix() {
    int i, j, k, l;

    for(l = 1; l < cnt_sub; ++l){
        for(i = 0; i < cnt_sub - l; ++i){
            j = i + l;
            dp[i][j] = 200000000;
            for(k = i; k < j; k++) dp[i][j] = std::min(dp[i][j], dp[i][k] + dp[k+1][j] + sub_matrix[i].first * sub_matrix[k].second * sub_matrix[j].second);
        }
    }
}

void sort_sub_matrix() {
    std::vector<std::pair<int, int>> new_sub_matrix;
    int prev_index;
    bool is_start;

    for (int i = 0; i < cnt_sub; ++i) {
        is_start = true;
        for (int j = 0; j < cnt_sub; ++j) {
            if (i == j) continue;
            if (sub_matrix[i].first == sub_matrix[j].second) {
                is_start = false;
                break;
            }
        }
        if (is_start) {
            prev_index = i;
            break;
        }
    }

    new_sub_matrix.emplace_back(sub_matrix[prev_index].first, sub_matrix[prev_index].second);
    for (int i = 0; i < cnt_sub - 1; ++i) {
        for (int j = 0; j < cnt_sub; ++j) {
            if (sub_matrix[j].first != sub_matrix[prev_index].second) continue;
            new_sub_matrix.emplace_back(sub_matrix[j].first, sub_matrix[j].second);
            prev_index = j;
        }
    }

    sub_matrix = new_sub_matrix;
}

void bfs(int r, int c) {
    int row = 0, col = 0, k;
    
    for (k = r; k < N; ++k) if (board[k][c] == 0) break; row = k;
    for (k = c; k < N; ++k) if (board[r][k] == 0) break; col = k;
    for (int i = r; i < row; ++i) for (int j = c; j < col; ++j) visit[i][j] = true;

    sub_matrix.emplace_back(row - r, col - c);
}

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);

	std::cin >> T;
	for(test_case = 1; test_case <= T; ++test_case) {
        sub_matrix.clear();
        std::cin >> N;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                std::cin >> board[i][j];
                visit[i][j] = false;
            }
        }

        //for (int i = 0; i < cnt_sub; ++i) dp[i][i] = 0;
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                if (board[i][j] != 0 && !visit[i][j]) bfs(i, j);
        
        cnt_sub = sub_matrix.size();
        sort_sub_matrix();
        chain_matrix();
        std::cout << "#" << test_case << ' ' << dp[0][cnt_sub-1] << '\n';
	}
	return 0;
}