#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

using pii = std::pair<int, int>;
using ll = long long;

bool compare(pii a, pii b) { return a.first > b.first; }

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, M, start, end, count = 0;
    
    std::cin >> N >> M;
    ll answer = M;
    pii arr[N];
    for (int i = 0; i < N; ++i) {
        std::cin >> start >> end;
        if (start > end) arr[count++] = {start, end};
    }

    std::sort(arr, arr + count, compare);
    start = arr[0].first, end = arr[0].second;
    for (int i = 1; i < count; ++i) {
        if (end <= arr[i].first) end = std::min(end, arr[i].second);
        else {
            answer += 2 * (start - end);
            start = arr[i].first;
            end = arr[i].second;
        }
    }

    std::cout << answer + 2 * (start - end);

    return 0;
}