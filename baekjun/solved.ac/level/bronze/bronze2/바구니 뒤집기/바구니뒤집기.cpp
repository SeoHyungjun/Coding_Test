#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, M, a, b, arr[100];

    std::cin >> N >> M;
    for (int i = 0; i < N; ++i) arr[i] = i + 1;

    while (M--) {
        std::cin >> a >> b;
        if (a == b) continue;

        int tmp;
        for (int i = a - 1, j = b - 1; i <= j; ++i, --j) {
            tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
    }

    for (int i = 0; i < N; ++i) std::cout << arr[i] << ' ';

    return 0;
}