#include <iostream>
#include <string>
#include <algorithm>

int main() {
    std::ios_base::sync_with_stdio(0);
	std::cin.tie(0), std::cout.tie(0);
    
    std::string n;
    int m;

    std::cin >> n >> m;
    int len = n.length();
    m = std::min(m, len*stoi(n));

    while (m >= len) {
        std::cout << n;
        m -= len;
    }
    for (int i = 0; i < m; i++) std::cout << n[i];

    return 0;
}