#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, M, A, B, cnt;
    bool graph[1000][1000];

    std::cin >> N >> M;
    while (M--) {
        std::cin >> A >> B;
        graph[A-1][B-1] = true;
        graph[B-1][A-1] = true;
    }

    for (int i = 0; i < N; ++i) {
        cnt = 0;
        for (int j = 0; j < N; ++j) if (graph[i][j]) ++cnt;
        std::cout << cnt << '\n';
    }

    return 0;
}
