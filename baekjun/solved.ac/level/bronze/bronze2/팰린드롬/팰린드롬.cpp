#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

bool is_palindrome(std::string s) {
    bool answer = true;

    for (int i = 0; i < s.length() / 2; ++i) {
        if (s[i] == s[s.length() - i - 1]) continue;
        answer = false;
        break;
    }

    return answer;
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N;
    std::string str;

    std::cin >> N;
    std::cin.ignore();
    while (N--) {
        std::getline(std::cin, str);
        std::transform(str.begin(), str.end(), str.begin(), ::tolower);
        std::cout << (is_palindrome(str)?"Yes\n":"No\n");
    }

    return 0;
}