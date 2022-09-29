#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int reverse(int n) {
    int result = 0;
    while (n) {
        result = result*10 + n%10;
        n/=10;
    }
    return result;
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, cur, sum;

    std::cin >> T;
    while (T--) {
        std::cin >> cur;
        sum = cur + reverse(cur);
        std::cout << (sum == reverse(sum) ? "YES" : "NO") << '\n'; 
    }

    return 0;
}