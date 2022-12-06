#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    long long N;

    std::cin >> N;
    std::cout << (N&1?"SK":"CY");

    return 0;
}