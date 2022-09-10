#include <iostream>
#include <string>

const int all_include = 0x3ffffff;
int bitmap[26], word2bit[15], answer, N;

void dfs(int idx, int cur) {
    if (cur == all_include) ++answer;
    for (int i = idx + 1; i < N; ++i) dfs(i, cur | word2bit[i]);
}

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
	int test_case, T, result;
    std::string str;

	//freopen("input.txt", "r", stdin);
    for (int i = 0; i < 26; ++i) bitmap[i] = 1 << i;
	std::cin >> T;
	for(test_case = 1; test_case <= T; ++test_case) {
        std::cin >> N;
        for (int i = 0; i < N; ++i) {
            std::cin >> str;
            result = 0;
            for (int j = 0; j < str.length(); ++j) result |= bitmap[str[j] - 'a'];
            word2bit[i] = result;
        }

        answer = 0;
        dfs(-1, 0);
        std::cout << '#' << test_case << ' ' << answer << '\n';
	}
	return 0;
}