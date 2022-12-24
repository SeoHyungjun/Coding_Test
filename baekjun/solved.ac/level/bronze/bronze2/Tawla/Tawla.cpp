#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

std::string dic1[7] = {"", "Yakk", "Doh", "Seh", "Ghar", "Bang", "Sheesh"};
std::string dic2[7] = {"", "Habb Yakk", "Dobara", "Dousa", "Dorgy", "Dabash", "Dosh"};

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, a, b;

    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        std::cin >> a >> b;

        if (a < b) std::swap(a, b);

        std::cout << "Case " << t << ": ";
        if (a == 6 && b == 5) std::cout << "Sheesh Beesh\n";
        else if (a == b) std::cout << dic2[a] << '\n';
        else std::cout << dic1[a] << ' ' << dic1[b] << '\n';
    }

    return 0;
}