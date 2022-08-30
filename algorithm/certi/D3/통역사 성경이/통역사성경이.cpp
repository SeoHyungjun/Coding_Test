#include <iostream>
#include <string>
#include <stdio.h>

int main(int argc, char** argv)
{
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
	int test_case, T, N, cnt_name, len_word, i, is_name;
	std::string answer = "", cur;
    bool is_end = false;

	//freopen("input.txt", "r", stdin);
    std::cin >> T;
	for (test_case = 1; test_case <= T; ++test_case) {
        std::cin >> N;
		answer += '#' + std::to_string(test_case) + ' ';

		cnt_name = 0;
		while (N) {
			std::cin >> cur;

            len_word = cur.length();
            is_name = 0;
            if (cur[0] >= 'A' && cur[0] <= 'Z') {
                for (i = 1; i < len_word; i++) {
                    if (cur[i] >= 'a' && cur[i] <= 'z') continue;
                    is_name = i;
                    break;
                }
                if (!is_name) cnt_name++;
            }
        
            if (cur[len_word - 1] == '.' || cur[len_word - 1] == '!' || cur[len_word - 1] == '?') {
                if (is_name == len_word-1) cnt_name++;
                N--;
                answer += std::to_string(cnt_name) + " ";
                cnt_name = 0;
            }
            
		}
		answer += '\n';
	}
	std::cout << answer;

	return 0;
}