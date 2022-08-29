#include<iostream>
#include<string>

int test_case, T, n, i, j, arr[10] = {0, };
std::string tmp[10] = {"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN" };
std::string answer = "", t;

int main(int argc, char** argv)
{
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
	
	std::cin >> T;
	for (test_case = 1; test_case <= T; ++test_case) {
		std::cin >> t >> n;

        while (n--) {
            std::cin >> t;
            if (t[0] == 'Z') arr[0]++;
            else if (t[0] == 'O') arr[1]++;
            else if (t[0] == 'T') {
                if (t[1] == 'W') arr[2]++;
                else arr[3]++;
            }
            else if (t[0] == 'F') {
                if (t[1] == 'O') arr[4]++;
                else arr[5]++;
            }
            else if (t[0] == 'S') {
                if (t[1] == 'I') arr[6]++;
                else arr[7]++;
            }
            else if (t[0] == 'E') arr[8]++;
            else if (t[0] == 'N') arr[9]++;
        }
		
		answer += '#' + std::to_string(test_case) + '\n';
		for (i = 0; i < 10; i++) {
            while (arr[i]) {
				answer += tmp[i] + ' ';
                arr[i]--;
			}
		}
		answer += '\n';
	}
    std::cout << answer;
	return 0;
}