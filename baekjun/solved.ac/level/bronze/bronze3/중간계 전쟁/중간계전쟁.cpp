#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int point_of_gandalf_side[6] = {1, 2, 3, 3, 4, 10};
int point_of_sauron_side[7] = {1, 2, 2, 2, 3, 5, 10};

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, gandalf, sauron, tmp;

    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        gandalf = 0;
        sauron = 0;
        for (int i = 0; i < 6; ++i) {
            std::cin >> tmp;
            gandalf += point_of_gandalf_side[i] * tmp;
        }
        for (int i = 0; i < 7; ++i) {
            std::cin >> tmp;
            sauron += point_of_sauron_side[i] * tmp;
        }

        std::cout << "Battle " << t << ": ";
        if (gandalf > sauron) std::cout << "Good triumphs over Evil\n";
        else if (gandalf < sauron) std::cout << "Evil eradicates all trace of Good\n";
        else std::cout << "No victor on this battle field\n";
    }

    return 0;
}