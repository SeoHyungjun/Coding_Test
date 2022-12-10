#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int num_weight, weights[30], num_ball, ball;
bool dp[31][15001]; // 추 1개 최대 500g * 30개 = 15000g

void solve(int i, int w) {
    if (num_weight < i || dp[i][w]) return;

    dp[i][w] = true;
    solve(i + 1, w); // i 번째 추 안올림
    solve(i + 1, w + weights[i]); // i 번째 추를 구슬 반대편에 올리기
    solve(i + 1, abs(w - weights[i])); // i 번째 추를 구슬 쪽에 올리기
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    
    std::cin >> num_weight;
    for (int i = 0; i < num_weight; ++i) std::cin >> weights[i];
    solve(0, 0);

    std::cin >> num_ball;
    while (num_ball--) {
        std::cin >> ball;

        if (ball > 15000) std::cout << "N ";
        else if (dp[num_weight][ball]) std::cout << "Y ";
        else std::cout << "N ";
    }

    return 0;
}