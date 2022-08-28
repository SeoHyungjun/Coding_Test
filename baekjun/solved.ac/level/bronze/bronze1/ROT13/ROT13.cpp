#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0);
	std::cin.tie(0), std::cout.tie(0);

    std::string str;

    getline(std::cin, str);
    for (int i = 0; i < str.length(); i++) {
        if (str[i] >= 'a' && str[i] <= 'z') {
            str[i] = (str[i] - 'a' + 13 + 26) % 26 + 'a';
        } else if (str[i] >= 'A' && str[i] <= 'Z') {
            str[i] = (str[i] - 'A' + 13 + 26) % 26 + 'A';
        } 
    }
    std::cout << str;

    return 0;
}