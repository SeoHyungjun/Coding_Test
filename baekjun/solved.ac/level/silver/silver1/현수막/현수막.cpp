#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <deque>

int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

int N, M;
bool board[250][250];

void bfs(int a, int b) {
    std::deque<std::pair<int, int>> q;
    q.emplace_back(a, b);

    while (!q.empty()) {
        int x = q.front().first, y = q.front().second;
        q.pop_front();

        for (int i = 0 ; i < 8; ++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (!(nx >= 0 && nx < N && ny >= 0 && ny < M)) continue;
            if (!board[nx][ny]) continue;
            q.emplace_back(nx, ny);
            board[nx][ny] = false;
        }
    }
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);

    std::cin >> N >> M;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j)
            std::cin >> board[i][j];
    }
    
    int answer = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (board[i][j]) {
                bfs(i, j);
                ++answer;
            }
        }
    }

    std::cout << answer;

    return 0;
}