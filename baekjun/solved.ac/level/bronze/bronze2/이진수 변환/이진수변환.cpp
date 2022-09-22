#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

std::string change_binary(long long num) {
    std::string result = "";

    while (num) {result += std::to_string(num & 1);num >>= 1;}
    std::reverse(result.begin(), result.end());

    return result;
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    long long N;

    std::cin >> N;
    std::cout << change_binary(N);

    return 0;
}