#include <iostream>
#include <algorithm>
 
int main() {
    int m, n, a=0, b=0, h, p;
    std::cin >> m >> n;
    for (int i = 0; i < m; i++){
        std::cin >> h;
        a = std::max(a, h);
    }
    for (int j = 0; j < n; j++) {
        std::cin >> p;
        b = std::max(b, p);
    }
    std::cout << a + b << '\n';
}