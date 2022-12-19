#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int A_attack, A_health, B_attack, B_health;

    std::cin >> A_attack >> A_health;
    std::cin >> B_attack >> B_health;

    while ((A_health > 0) & (B_health > 0)) {
        A_health -= B_attack;
        B_health -= A_attack;
    }

    if (A_health <= 0 && B_health <= 0) std::cout << "DRAW";
    else if (A_health > 0) std::cout <<"PLAYER A";
    else std::cout << "PLAYER B";

    return 0;
}