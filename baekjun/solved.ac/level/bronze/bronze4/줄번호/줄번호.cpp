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
        getline(std::cin, str);
        std::cin.clear();
        std::cout << i << ". " << str << '\n';
    }

    return 0;
}