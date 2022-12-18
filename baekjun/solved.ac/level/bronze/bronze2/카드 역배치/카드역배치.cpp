#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int arr[20], a, b;

    for (int i = 0; i < 20; ++i) arr[i] = i + 1;
    for (int i = 0; i < 10; ++i) {
        std::cin >> a >> b;
        std::reverse(arr + a - 1, arr + b);
    }

    for (int i = 0; i < 20; ++i) std::cout << arr[i] << ' ';

    return 0;
}