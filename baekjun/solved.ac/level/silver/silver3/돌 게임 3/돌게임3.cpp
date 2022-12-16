#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N;
    bool check[1001] = {false, };
    check[1] = check[3] = check[4] = true;

    std::cin >> N;
    for (int i = 5; i <= N; ++i) check[i] = !check[i - 1] | !check[i - 3] | !check[i - 4];

    std::cout << (check[N] ? "SK" : "CY");

    return 0;
}