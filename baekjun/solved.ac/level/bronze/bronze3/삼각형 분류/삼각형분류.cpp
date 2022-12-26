#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, arr[3];

    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        std::cin >> arr[0] >> arr[1] >> arr[2];
        std::sort(arr, arr + 3);

        std::cout << "Case #" << t << ": ";
        if (arr[2] >= arr[0] + arr[1]) std::cout << "invalid!\n";
        else if (arr[0] == arr[1] && arr[1] == arr[2]) std::cout << "equilateral\n";
        else if (arr[0] == arr[1] || arr[1] == arr[2]) std::cout << "isosceles\n";
        else std::cout << "scalene\n";
    }


    return 0;
}