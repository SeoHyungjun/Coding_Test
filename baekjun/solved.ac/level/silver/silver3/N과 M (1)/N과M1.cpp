#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>

bool check[9] = {false,};
std::vector<int> arr;

void dfs(int cnt, int N, int M) {
    if (cnt >= M) {
        for (auto& it: arr) std::cout << it << ' ';
        std::cout << '\n';
        return;
    }
    
    for (int i = 1; i <= N; ++i) {
        if (check[i]) continue;
        check[i] = true;
        arr.emplace_back(i);
        dfs(cnt+1, N, M);
        arr.pop_back();
        check[i] = false;
    }
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, M;

    std::cin >> N >> M;
    dfs(0, N, M);

    return 0;
}