#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, cnt_g, cnt_b;
    std::string name;

    std::cin >> N;
    std::cin.ignore();
    while (N--) {
        std::getline(std::cin, name);

        cnt_g = cnt_b = 0;
        for (int i = 0; i < name.length(); ++i) {
            if (name[i] == 'g' | name[i] == 'G') ++cnt_g;
            else if (name[i] == 'b' | name[i] == 'B') ++cnt_b;
        }

        std::cout << name << " is ";
        if (cnt_g > cnt_b) std::cout << "GOOD\n";
        else if (cnt_g < cnt_b) std::cout << "A BADDY\n";
        else std::cout << "NEUTRAL\n";
    }

    return 0;
}