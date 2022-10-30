#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <deque>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, K;
    std::string num;
    std::deque<char> q;

    std::cin >> N >> K;
    std::cin >> num;

    for (int i = 0; i < N; ++i) {
        while (K && !q.empty() && q.back() < num[i]) {
            q.pop_back();
            --K;
        }
        q.emplace_back(num[i]);
    }

    for (int i = 0; i < q.size() - K; ++i) std::cout << q[i];

    return 0;
}