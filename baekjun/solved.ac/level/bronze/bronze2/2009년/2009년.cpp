#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int days[13] = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365};
std::string answer[7] = {"Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"};

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);

    int D, M, cur;
    std::cin >> D >> M;

    cur = days[M-1] + D - 1;
    std::cout << answer[cur % 7];

    return 0;
}