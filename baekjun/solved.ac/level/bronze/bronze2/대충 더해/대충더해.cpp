#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string answer = "", a, b;

    std::cin >> a >> b;
    std::reverse(a.begin(), a.end());
    std::reverse(b.begin(), b.end());

    for (int i = 0; i < std::min(a.length(), b.length()); ++i) answer = std::to_string((a[i] - '0')+(b[i] - '0')) + answer;
    for (int i = std::min(a.length(), b.length()); i < std::max(a.length(), b.length()); ++i) {
        if (a.length() < b.length()) answer = b[i] + answer;
        else answer = a[i] + answer;
    }
    std::cout << answer;

    return 0;
}