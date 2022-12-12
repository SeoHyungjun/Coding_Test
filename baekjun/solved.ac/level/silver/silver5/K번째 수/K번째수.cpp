#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int N, K, arr[5000000];

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    
    std::cin >> N >> K;
    for (int i = 0; i < N; ++i) std::cin >> arr[i];
    std::sort(arr, arr + N);

    std::cout << arr[K-1];

    return 0;
}