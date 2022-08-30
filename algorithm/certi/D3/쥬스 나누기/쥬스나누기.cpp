#include <iostream>
#include <string>

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
	int test_case, T, N;
    std::string answer = "";

	std::cin>>T;
	for(test_case = 1; test_case <= T; ++test_case) {
        std::cin >> N;

        answer += "#" + std::to_string(test_case) + " ";
        for (int i = 0; i < N; ++i) {
            answer += "1/" + std::to_string(N) + " ";
        }
        answer += '\n';
	}
    std::cout << answer;

	return 0;
}