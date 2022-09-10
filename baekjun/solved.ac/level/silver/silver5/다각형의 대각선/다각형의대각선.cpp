#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N;

    std::cin >> N;
    std::cout << N * (N-1) * (N-2) * (N-3) / 24;

    return 0;
}