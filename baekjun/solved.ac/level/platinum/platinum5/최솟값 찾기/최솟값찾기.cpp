#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <deque>

int N, L, arr[5000000];
using pii = std::pair<int, int>;

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);

    std::cin >> N >> L;
    for (int i = 0; i < N; ++i) std::cin >> arr[i];

    std::deque<pii> q;
    for (int i = 0; i < N; ++i) {
        while (!q.empty() && q.front().second < i - L + 1) q.pop_front();
        while (!q.empty() && q.back().first > arr[i]) q.pop_back();
        q.emplace_back(arr[i], i);
        std::cout << q.front().first << " ";
    }

    return 0;
}