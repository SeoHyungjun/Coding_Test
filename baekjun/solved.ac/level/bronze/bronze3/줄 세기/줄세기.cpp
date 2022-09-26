#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;
    int answer = 0;

    while (std::getline(std::cin, str)) ++answer;
    
    std::cout << answer;

    return 0;
}