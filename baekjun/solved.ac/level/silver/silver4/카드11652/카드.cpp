#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <unordered_map>

using ll = long long;

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, last = 0;
    ll cur;
    std::unordered_map<ll, int> dic;

    std::cin >> N;
    for (int i = 0; i < N; ++i) {
        std::cin >> cur;
        ++dic[cur];
    }

    int max_cnt = 0;
    ll answer = 0;
    for (auto it = dic.begin(); it != dic.end(); ++it) {
        if (it->second < max_cnt) continue;
        else if (it->second == max_cnt) answer = std::min(answer, it->first);
        else {
            answer = it->first;
            max_cnt = it->second;
        }
    }

    std::cout << answer;

    return 0;
}