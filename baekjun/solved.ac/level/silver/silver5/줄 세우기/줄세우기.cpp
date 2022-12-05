#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N;
    std::string str[20];
    bool is_increasing = true, is_decreasing = true;

    std::cin >> N;
    for (int i = 0; i < N; ++i) std::cin >> str[i];
    for (int i = 1; i < N; ++i) {
        if (str[i - 1] < str[i]) is_decreasing = false;
        if (str[i - 1] > str[i]) is_increasing = false;
    }

    if (!is_increasing && !is_decreasing) std::cout << "NEITHER";
    else if (is_increasing) std::cout << "INCREASING";
    else std::cout << "DECREASING";

    return 0;
}