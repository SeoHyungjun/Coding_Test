#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;
    int i, happy = 0, sad = 0;

    std::getline(std::cin, str);
    for (i = 0; i < str.length() - 2; ++i) {
        if (str[i] != ':' or str[i+1] != '-') continue;
        if (str[i+2] == ')') ++happy;
        else if (str[i+2] == '(') ++sad;
    }

    if (happy == 0 && sad == 0) std::cout << "none";
    else if (happy == sad) std::cout << "unsure";
    else if (happy > sad) std::cout << "happy";
    else if (happy < sad) std::cout << "sad";

    return 0;
}