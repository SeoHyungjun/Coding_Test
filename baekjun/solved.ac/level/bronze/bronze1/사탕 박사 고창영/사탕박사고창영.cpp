#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int t, r, c;
    std::string board[401], white;

    std::cin >> t;

    while (t--) {
        int answer = 0;

        std::cin >> r >> c;
        std::cin.ignore();
        for (int i = 0; i < r; ++i) {
            std::getline(std::cin, board[i]);
        }

        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c - 2; ++j) {
                if (board[i][j] == '>' && board[i][j+1] == 'o' && board[i][j+2] == '<') ++answer; 
            }
        }

        for (int i = 0; i < r-2; ++i) {
            for (int j = 0; j < c; ++j) {
                if (board[i][j] == 'v' && board[i+1][j] == 'o' && board[i+2][j] == '^') ++answer;
            }
        }
        
        std::cout << answer << '\n';
    }

    return 0;
}