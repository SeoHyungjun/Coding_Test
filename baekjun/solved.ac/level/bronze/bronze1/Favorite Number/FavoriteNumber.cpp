#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, V, S;

    std::cin >> N;
    while (N--) {
        std::cin >> V;
        int arr[1001] = {0, };
        for (int i = 0; i < V; ++i) {
            std::cin >> S;
            ++arr[S];
        }

        int cnt = 0, answer = 0;
        for (int i = 1; i < 1001; ++i) {
            if (arr[i] <= cnt) continue;
            cnt = arr[i];
            answer = i;
        }

        std::cout << answer << '\n';
    }

    return 0;
}