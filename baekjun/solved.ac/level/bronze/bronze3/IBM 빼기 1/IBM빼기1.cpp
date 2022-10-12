#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N;
    std::string str;

    std::cin >> N;
    std::cin.ignore();
    for (int i = 1; i <= N; ++i) {
        std::cin >> str;
        std::cout << "String #" << i << "\n";
        for (int j = 0; j < str.length(); ++j) {
            std::cout << (char)((str[j] - 'A' + 1) % 26 + 'A');
        }
        std::cout << "\n\n";
    }

    return 0;
}