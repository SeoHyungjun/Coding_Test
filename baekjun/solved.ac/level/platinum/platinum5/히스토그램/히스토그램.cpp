#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <stack>

int N, answer = 0, arr[100002] = {0,};
std::stack<int> s;

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);

    std::cin >> N;
    for (int i = 1; i <= N; ++i) std::cin >> arr[i];

    s.emplace(0);
    for (int i = 1; i <= N + 1; ++i) {
        while (!s.empty() && arr[s.top()] > arr[i]) {
            int cur_top = s.top();
            s.pop();
            answer = std::max(answer, arr[cur_top] * (i - s.top() - 1));
        }

        s.emplace(i);
    }

    std::cout << answer;

    return 0;
}