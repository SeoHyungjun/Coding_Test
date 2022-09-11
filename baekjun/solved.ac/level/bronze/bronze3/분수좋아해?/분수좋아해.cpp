#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int a, b, carry;

    while (1) {
        std::cin >> a >> b;
        if (a == 0 && b == 0) break;

        carry = 0;
        if (a >= b) {
            carry = a / b;
            a %= b;
        }

        std::cout << carry << ' ' << a << " / " << b << '\n';
        }

    return 0;
}