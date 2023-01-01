#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    char a;

    std::cin >> a;
    std::cout << (a == 'n' || a == 'N' ? "Naver D2" : "Naver Whale");

    return 0;
}