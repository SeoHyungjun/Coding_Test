#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, cur;
    std::string str;
    
    std::cin >> N;
    while (N--) {
        std::cin >> str;
        cur = str[str.length() - 1] -'0';
        std::cout << (cur & 1? "odd" : "even" ) << '\n';
    }

    return 0;
}