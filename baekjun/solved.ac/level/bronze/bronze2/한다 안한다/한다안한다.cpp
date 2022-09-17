#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, mid;
    std::string str;

    std::cin >> N;
    while (N--) {
        std::cin >> str;
        mid = str.length()/2;
        std::cout << (str[mid-1] == str[mid] ? "Do-it\n" : "Do-it-Not\n");
    }

    return 0;
}