#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    bool A, B, C;

    std::cin >> A >> B >> C;

    if (A == B && B == C) std::cout << "*";
    else if (A == B) std::cout << "C";
    else if (A == C) std::cout << "B";
    else if (B == C) std::cout << "A";

    return 0;
}