#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N;
    std::string str1, str2;
    bool flag = true, answer = true;

    std::cin >> N >> str1 >> str2;
    if (N % 2 == 1) flag = false;
    for (int i = 0; i < str1.length(); i++) {
        if ((flag && str1[i] == str2[i]) || (!flag && str1[i] != str2[i])) continue;
        answer = false;
        break;
    }

    if (answer) std::cout << "Deletion succeeded";
    else std::cout << "Deletion failed";

    return 0;
}