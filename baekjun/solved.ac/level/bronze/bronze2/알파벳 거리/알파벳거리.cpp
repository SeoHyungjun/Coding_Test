#include <iostream>
#include <string>
#include <algorithm>

int main() {
    std::ios_base::sync_with_stdio(0);
	std::cin.tie(0), std::cout.tie(0);
    
    int t;
    std::string x, y;

    std::cin >> t;
    while (t--) {
        std::cin >> x >> y;

        std::cout << "Distances: ";
        for (int i = 0; i < x.length(); i++) std::cout << (int(y[i] - x[i]) + 26) % 26 << ' ';
        std:: cout << '\n';
    }
    
    return 0;
}