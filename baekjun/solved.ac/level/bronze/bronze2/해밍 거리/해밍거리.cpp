#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, cnt;
    std::string a, b;

    std::cin >> T;
    while (T--) {
        std::cin >> a >> b;

        cnt = 0;
        for (int i = 0; i < a.length(); ++i) if (a[i] != b[i]) ++cnt;

        std::cout << "Hamming distance is " << cnt << ".\n";
    }

    return 0;
}