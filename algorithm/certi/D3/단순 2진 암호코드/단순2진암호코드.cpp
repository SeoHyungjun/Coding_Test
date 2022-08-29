#include<iostream>
#include <string>

std::string dic[10] = {"0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"};

int main(int argc, char** argv)
{
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    
	int test_case, T, N, M, end;
    std::string str, cur_num, last_answer = "";
	
	std::cin>>T;
	for(test_case = 1; test_case <= T; ++test_case) {
        bool flag = false;
        int answer[8] = {0, }, crypto, cur_sum = 0;
        std::cin >> N >> M;

        while (N--) {
            std::cin >> str;
            if (flag) continue;

            for (int i = str.length() - 1; i >= M - 56; i--) {
                if (str[i] == '0') continue;
                flag = true;
                end = i;
                break;
            }

            if (!flag) continue;
            
            for (int i = end - 55, k = 0; i < end; i+=7, k++) {
                cur_num = "";
                for (int j = 0; j < 7; j++) cur_num += str[i+j];
                
                for (int j = 0; j < 10; j++) {
                    if (cur_num != dic[j]) continue;
                    answer[k] = j;
                    cur_sum += j;
                    break;
                }
            }
            
            crypto = (answer[0] + answer[2] + answer[4] + answer[6]) * 3 + (answer[1] + answer[3] + answer[5] + answer[7]);
        }
        if (crypto % 10 != 0) last_answer += "#" + std::to_string(test_case) + " 0\n";
        else last_answer += "#" + std::to_string(test_case) + " " + std::to_string(cur_sum) + "\n";
	}
    std::cout << last_answer;

	return 0;
}