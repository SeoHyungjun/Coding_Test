#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int A[10], B[10], a = 0, b = 0;

    for (int i = 0; i < 10; ++i) std::cin >> A[i];
    for (int i = 0; i < 10; ++i) std::cin >> B[i];
    for (int i = 0; i < 10; ++i) {
        if (A[i] > B[i]) ++a;
        else if (A[i] < B[i]) ++b;
    }

    if (a > b) std::cout << 'A';
    else if (a < b) std::cout << 'B';
    else std::cout << 'D';

    return 0;
}