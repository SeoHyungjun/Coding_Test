#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int A, B, arr[1001], answer = 0, cnt = -1, cur = 1;

    std::cin >> A >> B;
    while (cnt < 1000) {
        for (int i = 0; i < cur && cnt < 1000; ++i) arr[++cnt] = cur;
        ++cur;
    }

    for (int i = A - 1; i < B; ++i) answer += arr[i];
    std::cout << answer;

    return 0;
}