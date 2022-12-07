#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, M;
    std::string a[10], b[10];
    bool flag = true;

    std::cin >> N >> M;
    for (int i = 0; i < N; ++i) std::cin >> a[i];
    for (int i = 0; i < N; ++i) std::cin >> b[i];

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (a[i][j] == b[i][2 * j] && a[i][j] == b[i][2 * j + 1]) continue;
            flag = false;
            break;
        }
        if (!flag) break;
    }

    std::cout << (flag?"Eyfa":"Not Eyfa");

    return 0;
}