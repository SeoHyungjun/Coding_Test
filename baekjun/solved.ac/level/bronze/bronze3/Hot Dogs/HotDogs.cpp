#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    double H, P;

    while (~scanf("%lf %lf", &H, &P)) {
        printf("%.2f\n", H / P);
    }

    return 0;
}