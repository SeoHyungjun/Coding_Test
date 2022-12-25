#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int K, h;
    std::string str;

    std::cin >> K;
    for (int i = 1; i <= K; ++i) {
        std::cin >> h;
        std::cin >> str;

        for (int j = 0; j < str.length(); ++j) {
            if (str[j] == 'c') ++h;
            else --h;
        }

        std::cout << "Data Set " << i << ":\n";
        std::cout << h << "\n\n";

    }
    return 0;
}