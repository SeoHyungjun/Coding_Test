#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int a, b;
    char com;

    std::cin >> a;
    std::cin.ignore();
    while (true) {
        std::cin >> com;
        if (com == '=') break;
        std::cin >> b;
        std::cin.ignore();

        if (com == '+') a += b;
        else if (com == '-') a -= b;
        else if (com == '*') a *= b;
        else a /= b;
    }

    std::cout << a;

    return 0;
}