#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int N, M, arr[7];

void dfs(int cnt) {
    if (cnt == M) {
        for (int i = 0; i < M; ++i) std::cout << arr[i] << ' ';
        std::cout << '\n';
        return;
    }
    
    for (int i = 1; i <= N; ++i) {
        arr[cnt] = i;
        dfs(cnt + 1);
    }
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    
    std::cin >> N >> M;
    dfs(0);

    return 0;
}