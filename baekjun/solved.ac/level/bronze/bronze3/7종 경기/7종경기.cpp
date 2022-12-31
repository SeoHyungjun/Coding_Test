#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, arr[7], answer;

    std::cin >> T;
    while (T--) {
        for (int i = 0; i < 7; ++i) std::cin >> arr[i];
        answer = 9.23076 * pow(26.7 - arr[0], 1.835);
        answer += 4.99087 * pow(42.5 - arr[3], 1.81);
        answer += 0.11193 * pow(254 - arr[6], 1.88);

        answer += 1.84523 * pow(arr[1] - 75, 1.348); 
        answer += 56.0211 * pow(arr[2] - 1.5, 1.05);
        answer += 0.188807 * pow(arr[4] - 210, 1.41);
        answer += 15.9803 * pow(arr[5] - 3.8, 1.04);

        std::cout << answer << '\n';
    }

    return 0;
}