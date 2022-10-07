#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int table[10] = {0, };

void make_table(std::string pattern) {
    int pattern_size = pattern.length(), j = 0;
    for (int i = 1; i < pattern_size; ++i) {
        while (j > 0 && pattern[i] != pattern[j]) j = table[j-1];
        if (pattern[i] == pattern[j]) table[i] = ++j;
    }
}

bool KMP(std::string pattern, std::string str) {
    int str_size = str.length(), pattern_size = pattern.length();
    int j = 0;
    for (int i = 0; i < str_size; ++i) {
        while (j > 0 && str[i] != pattern[j]) j = table[j-1];
        if (str[i] == pattern[j]) {
            if (j == pattern_size - 1) return true;
            ++j;
        }
    }
    return false;
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string pattern, str;
    int N, answer = 0;

    std::cin >> pattern;
    std::cin >> N;
    std::cin.ignore();
    make_table(pattern);
    while (N--) {
        std::cin >> str;
        str += str;
        if (KMP(pattern, str)) ++answer;
    }

    std::cout << answer;

    return 0;
}