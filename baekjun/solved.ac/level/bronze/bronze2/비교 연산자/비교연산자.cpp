#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int a, b, t = 0;
    std::string str;

    for (t = 1; ;++t) {
        bool flag;
        std::cin >> a >> str >> b;

        if (str == "E") break;
        
        if (str == ">") {
            flag = a > b;
        }
        else if (str == ">=") {
            flag = a >= b;
        }
        else if (str == "<") {
            flag = a < b;
        }
        else if (str == "<=") {
            flag = a <= b;
        }
        else if (str == "==") {
            flag = a == b;
        }
        else if (str == "!=") {
            flag = a != b;
        }
        std::cout << "Case " << t << ": " << (flag ? "true" : "false") << '\n';
    }

    return 0;
}