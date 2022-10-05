#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int K, cnt_A = 1, cnt_B = 0, tmp = 0;

    std::cin >> K;
    while (K--) {
        tmp = cnt_A;
        cnt_A = cnt_B;
        cnt_B = tmp + cnt_A;
    }

    std::cout << cnt_A << " " << cnt_B;

    return 0;
}


/*
A       B
1       0
0       1
1       1
1       2
2       3
*/