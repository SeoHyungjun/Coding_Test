#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <cstring>

char* next_word(char* str) {
    int length = strlen(str);
    int left = length - 1;
    while (left > 0 && str[left - 1] >= str[left]) --left;

    if (!left) return str;

    int right = length - 1;
    while (str[left - 1] >= str[right]) --right;
    
    std::swap(str[left - 1], str[right]);
    std::sort(str + left, str + length);
    
    return str;
}   

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T;
    char str[101];

    std::cin >> T;
    while (T--) {
        std::cin >> str;
        std::cout << next_word(str) << '\n';
    }

    return 0;
}