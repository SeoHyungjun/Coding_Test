#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, C, V;

    std::cin >> T;
    while(T--) {
        std::cin >> C >> V;
        std::cout << "You get " << C / V << " piece(s) and your dad gets " << C % V << " piece(s).\n";
    }

    return 0;
}