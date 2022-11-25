#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

long long gaus(long long a) {
    return a * (a+1) / 2;
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T;
    long long N, M, answer;

    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        std::cin >> N >> M;

        if (N == 0) answer = gaus(M);
        else if (N > 0) answer = gaus(M) - gaus(N - 1);
        else if (N < 0 && M + N >= 0) answer = gaus(M) - gaus(-N);
        else answer = -(gaus(-N) - gaus(M));

        if (t != 1) std::cout << "\n";
        std::cout << "Scenario #" << t << ":\n";
        std::cout << answer << "\n";
    }

    return 0;
}
