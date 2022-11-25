#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, M, a, b, c, arr[100] = {0, };

    std::cin >> N >> M;
    while (M--) {
        std::cin >> a >> b >> c;
        for (int i = a - 1; i < b; ++i) arr[i] = c;
    }

    for (int i = 0; i < N; ++i) std::cout << arr[i] << ' ';

    return 0;
}