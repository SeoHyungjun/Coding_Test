#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str, arr[1001];

    std::cin >> str;
    arr[str.length() - 1] = str[str.length() - 1];
    for (int i = str.length() - 1; i >= 0; --i) arr[i] = str[i] + arr[i+1];
    std::sort(arr, arr + str.length());

    for (int i = 0; i < str.length(); ++i) std::cout << arr[i] << '\n';

    return 0;
}