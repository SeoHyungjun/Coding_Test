#include <iostream>
#include <cmath>
#include <vector>

bool not_prime[10000001] = {false, };
std::string print_answer = "";
std::vector<int> prime;

void is_not_prime() {
    not_prime[1] = not_prime[0] = true;
    for (int i = 2; i <= sqrt(10000001); ++i) {
        if (not_prime[i]) continue;
        for (int j = i + i; j < 10000001; j+=i) not_prime[j] = true;
    }
}

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
	int test_case, T, A, answer, cnt, i;

    is_not_prime();
    for (i = 2; i < 10000001; ++i) if (!not_prime[i]) prime.emplace_back(i);

	std::cin >> T;
	for(test_case = 1; test_case <= T; ++test_case) {
        std::cin >> A;

        answer = 1;

        if (!not_prime[A]) {
            print_answer += "#" + std::to_string(test_case) + " " + std::to_string(A) + "\n";
            continue;
        }
        if (sqrt(A) != int(sqrt(A))) {
            for (auto& cur : prime) {
                cnt = 0;
                while (A % cur == 0) {
                    A /= cur;
                    ++cnt;
                }
                if (cnt % 2 != 0) answer *= cur;
                if (A == 1 || A < cur) break; 
                if (!not_prime[A]) break;
            }        
            if (A > 1) answer *= A;
        }

        //std::cout << "#" << test_case << " " << answer << '\n';
        print_answer += "#" + std::to_string(test_case) + " " + std::to_string(answer) + "\n";
	}
    std::cout << print_answer;
	return 0;
}