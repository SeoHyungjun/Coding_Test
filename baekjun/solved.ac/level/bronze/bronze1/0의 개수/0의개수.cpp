#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int cnt_zero(int n) {
    int cnt = 0;

    if (!n) return 1;
    while (n) {
        if (!(n % 10)) cnt += 1;
        n /= 10;
    }

    return cnt;
}

int main() {
    std::ios_base::sync_with_stdio(0);
	std::cin.tie(0), std::cout.tie(0);
    
    int t;

    std::cin >> t;
    while (t--) {
        int n, m, answer = 0;

        std::cin >> n >> m;
        for (int i = n; i <= m; i++) answer += cnt_zero(i);
        std::cout << answer << '\n';
    }
    
    return 0;
}