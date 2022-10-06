#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

long long arr[68];

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, N;

    arr[0] = arr[1] = 1;
    arr[2] = 2;
    arr[3] = 4;
    for (int i = 4; i < 68; ++i) arr[i] = arr[i-1] + arr[i-2] + arr[i-3] + arr[i-4];

    std::cin >> T;
    while (T--) {
        std::cin >> N;
        std::cout << arr[N] << "\n";
    }

    return 0;
}