#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int arr[3];
    std::string str;

    std::cin >> arr[0] >> arr[1] >> arr[2];
    std::cin >> str;

    std::sort(arr, arr+3);
    for (int i = 0; i < 3; ++i) std::cout << arr[str[i] - 'A'] << ' ';

    return 0;
}