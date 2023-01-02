#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>

int arr[9];
bool check[9] = {false, };
int N;

void dfs(int idx) {
    if (idx >= N) {
        for (int i = 0; i < N; ++i) {
            std::cout << arr[i] << ' ';
        }
        std::cout << '\n';
    }

    for (int i = 1; i <= N; ++i) {
        if (check[i]) continue;
        check[i] = true;
        arr[idx] = i;
        dfs(idx + 1);
        check[i] = false;
    }
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);

    std::cin >> N;
    dfs(0);

    return 0;
}