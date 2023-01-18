#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int R, C, ZR, ZC;
    char arr[50][50];

    std::cin >> R >> C >> ZR >> ZC;
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            std::cin >> arr[i][j];
        }
    }
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < ZR; ++j) {
            for (int k = 0; k < C; ++k) {
                for (int l = 0; l < ZC; ++l) {
                    std::cout << arr[i][k];
                }
            }
            std::cout << '\n';
        }
    }

    return 0;
}