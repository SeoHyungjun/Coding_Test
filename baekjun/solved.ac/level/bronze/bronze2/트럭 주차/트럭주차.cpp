#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int cost[4] = {0, }, start, end, arr[100] = {0, }, answer = 0;

    std::cin >> cost[1] >> cost[2] >> cost[3];
    for (int i = 0; i < 3; ++i) {
        std::cin >> start >> end;
        for (int j = start; j < end; ++j) ++arr[j];
    }

    for (int i = 0; i < 100; ++i) {
        answer += cost[arr[i]] * arr[i];
    }

    std::cout << answer;

    return 0;
}