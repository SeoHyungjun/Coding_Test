#include <iostream>
#include <string>
#include <vector>

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);

	int test_case, T, len, i, j, cnt, t;
    std::string print_answer = "", pattern, sentence;

	for(test_case = 1; test_case <= 10; ++test_case) {
        std::cin >> t >> pattern >> sentence;

        cnt = 0;
        len = pattern.length();
        std::vector<int> fail_function(len, 0);
        for (i = 1, j = 0; i < len; ++i) {
            while (j > 0 && pattern[i] != pattern[j]) j = fail_function[j-1];
            if (pattern[i] == pattern[j]) fail_function[i] = ++j;
        }

        for (i = 0, j = 0; i < sentence.length(); ++i) {
            while (j > 0 && sentence[i] != pattern[j]) j = fail_function[j-1];
            if (sentence[i] == pattern[j]) {
                if (j == len-1) {
                    ++cnt;
                    j = fail_function[j];
                }
                else ++j;
            }
        }

        print_answer += '#' + std::to_string(test_case) + ' ' + std::to_string(cnt) + '\n';
	}
    std::cout << print_answer;

	return 0;
}