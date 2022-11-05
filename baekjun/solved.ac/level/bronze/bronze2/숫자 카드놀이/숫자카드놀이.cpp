#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int play(int num) {
    int played_num = 1;

    while (num) {
        played_num *= num % 10;
        num /= 10;
    }

    return played_num;
}


int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N;

    while (true) {
        std::cin >> N;
        if (!N) break;

        while (true) {
            std::cout << N << ' ';
            if (N < 10) break;
            N = play(N);
        }
        std::cout << '\n';
    }

    return 0;
}