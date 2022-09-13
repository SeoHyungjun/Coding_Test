extern bool checkCards(int mIndexA, int mIndexB, int mDiff);
#include <vector>
#define rint register int

std::vector<int> abs_diff[50000];

int binary_search(int idx, int N) {
    int left = 0, right = N, mid;
    while (left < right) {
        mid = (left + right) / 2;
        if (checkCards(0, idx, mid)) right = mid;
        else left = mid + 1;
    }
    return left;
}

void playGame(int N) {
    for (rint i = 1; i < N + N; ++i) abs_diff[binary_search(i, N)].emplace_back(i);

    checkCards(0, *abs_diff[0].begin(), 0); abs_diff[0].clear();
    for (rint i = 1; i < N; ++i) {
        while (!abs_diff[i].empty()) {
            auto cur = abs_diff[i].begin(), next = cur + 1;
            while (!checkCards(*cur, *next, 0)) ++next;
            abs_diff[i].erase(next); abs_diff[i].erase(cur);
        }
    }
}