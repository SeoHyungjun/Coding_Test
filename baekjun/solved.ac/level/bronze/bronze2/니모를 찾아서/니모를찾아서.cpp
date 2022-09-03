#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;

    while (1) {
        getline(std::cin, str);
        if (str == "EOI") break;

        std::transform(str.begin(), str.end(), str.begin(), toupper);

        if (str.find("NEMO") != std::string::npos) std::cout << "Found\n";
        else std::cout << "Missing\n";
    }

    return 0;
}