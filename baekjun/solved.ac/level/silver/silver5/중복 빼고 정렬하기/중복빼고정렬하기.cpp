#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, cur;
    bool arr[2001] = {false, };

    std::cin >> N;
    while (N--) {
        std::cin >> cur;
        if (arr[cur + 1000]) continue;
        arr[cur + 1000] = true;
    }
    for (int i = -1000; i < 1001; ++i) {
        if (!arr[i + 1000]) continue;
        std::cout << i << ' ';
    }

    return 0;
}
