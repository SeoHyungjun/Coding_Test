#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

bool is_prime(int n) {
    bool not_prime[2000] = {false, };
    
    for (int i = 2; i < int(sqrt(2000)) + 1; ++i) {
        if (not_prime[i]) continue;
        for (int j = i + i; j < 2000; j += i) not_prime[j] = true;
    }

    return !not_prime[n];
}

bool is_prime_word(std::string s) {
    int sum = 0;

    for (int i = 0; i < s.length(); ++i) {
        if (s[i] >= 'a' && s[i] <= 'z') sum += s[i] - 'a' + 1;
        else sum += s[i] - 'A' + 27;
    }

    return is_prime(sum);
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;

    std::cin >> str;
    std::cout << (is_prime_word(str) ? "It is a prime word." : "It is not a prime word.");

    return 0;
}