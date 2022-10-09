#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T, N, vote, vote_sum, max_vote, max_vote_index;

    std::cin >> T;
    while (T--) {
        std::cin >> N;
        vote_sum = 0;
        max_vote = 0;
        max_vote_index = -1;
        for (int i = 1; i <= N; ++i) {
            std::cin >> vote;
            vote_sum += vote;
            if (vote > max_vote) {
                max_vote = vote;
                max_vote_index = i;
            }
            else if (vote == max_vote) {
                max_vote_index = -1;
            }
        }

        if (max_vote_index == -1) std::cout << "no winner" << '\n';
        else {
            if (vote_sum / 2 < max_vote) std::cout << "majority winner " << max_vote_index << '\n';
            else std::cout << "minority winner " << max_vote_index << '\n';
        }
    }

    return 0;
}