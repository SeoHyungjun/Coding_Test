#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <unordered_map>

using pii = std::pair<int, int>;
int arr[5][5], N, answer;

bool check() {
    int bingo = 0;

    for (int i = 0; i < 5; ++i) {
        int row = 0, col = 0;
        for (int j = 0; j < 5; ++j) {
            if (arr[i][j] == 0) ++row;
            if (arr[j][i] == 0) ++col;
        }
        if (row == 5) ++bingo;
        if (col == 5) ++bingo;
    }

    int left = 0, right = 0;
    for (int i = 0; i < 5; ++i) {
        if (arr[i][i] == 0) ++left;
        if (arr[4 - i][i] == 0) ++right;
    }
    if (left == 5) ++bingo;
    if (right == 5) ++bingo;

    return bingo >= 3 ? true : false;
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::unordered_map<int, pii> dic;
    bool flag = true;

    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            std::cin >> arr[i][j];
            dic.emplace(arr[i][j], std::make_pair(i, j));
        }
    }

    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            std::cin >> N;

            auto cur = dic[N];
            arr[cur.first][cur.second] = 0;

            if (flag & check()) {
                std::cout << i * 5 + j + 1;
                flag = false;
            }
        }
    }

    return 0;
}