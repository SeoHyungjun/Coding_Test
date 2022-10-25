#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

bool board[5001][5001] = {false, }, move;

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, M, x = 0, y = 0, nx, ny, direction = 0, cnt_change_direction;
    int dx[4] = {0, 1, 0, -1}, dy[4] = {1, 0, -1, 0};

    std::cin >> N >> M; // N : col, M : row
    board[0][0] = true;
    while (true) {        
        nx = x + dx[direction];
        ny = y + dy[direction];
        if (0 <= nx && nx < M && 0 <= ny && ny < N && !board[nx][ny]) {
            x = nx;
            y = ny;
            board[nx][ny] = true;
            continue;
        }
        
        direction = (direction + 1) % 4;
        nx = x + dx[direction];
        ny = y + dy[direction];
        if (0 <= nx && nx < M && 0 <= ny && ny < N && !board[nx][ny]) {
            x = nx;
            y = ny;
            board[nx][ny] = true;
        }
        else break;
    }

    std::cout << y << " " << x;

    return 0;
}