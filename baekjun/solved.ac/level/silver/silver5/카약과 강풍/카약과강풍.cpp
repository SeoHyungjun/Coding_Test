#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, S, R, kayak[11], cur, answer = 0;

    std::cin >> N >> S >> R;
    for (int i = 0; i < N; ++i) kayak[i] = 1;
    while (S--) {std::cin >> cur;--kayak[cur-1];}
    while (R--) {std::cin >> cur;++kayak[cur-1];}

    for (int i = 0; i < N; ++i) {
        if (kayak[i] < 2) continue;
        if (i > 0 && kayak[i-1] == 0) {
            ++kayak[i-1];
            --kayak[i];
        }
        else if (i+1 < N && kayak[i+1] == 0) {
            ++kayak[i+1];
            --kayak[i];
        }
    }

    for (int i = 0; i < N; ++i) if (kayak[i] == 0) ++answer;
    std::cout << answer;

    return 0;
}