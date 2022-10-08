#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T;
    float val;
    std::string str;
    std::cout << std::fixed;
    std::cout.precision(4);

    std::cin >> T;
    while (T--) {
        std::cin >> val >> str;
        if (str == "kg") {
            str = "lb";
            val *= 2.2046;
        }
        else if (str == "lb") {
            str = "kg";
            val *= 0.4536;
        }
        else if (str == "l") {
            str = "g";
            val *= 0.2642;
        }
        else if (str == "g") {
            str = "l";
            val *= 3.7854;
        }

        std::cout << val << " " << str << "\n";
    }

    return 0;
}