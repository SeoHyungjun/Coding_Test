#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N;
    std::string str;

    std::cin >> N;
    while (N--) {
        std::cin >> str;

        if (str == "P=NP") std::cout << "skipped\n";
        else {
            int a = 0, b = 0;
            for (int i = 0; i < str.length(); ++i) {
                if (str[i] == '+') {
                    a = b;
                    b = 0;
                    continue;
                }
                b = b*10 + str[i] - '0';
            }
            std::cout << a + b << '\n';
        }
    }
    return 0;
}