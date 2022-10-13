#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, M, arr[100], a, b, tmp;

    std::cin >> N >> M;
    for (int i = 0; i < N; ++i) arr[i] = i+1;
    while (M--) {
        std::cin >> a >> b;
        tmp = arr[a-1];
        arr[a-1] = arr[b-1];
        arr[b-1] = tmp;
    }

    for (int i = 0; i < N; ++i) std::cout << arr[i] << " ";

    return 0;
}