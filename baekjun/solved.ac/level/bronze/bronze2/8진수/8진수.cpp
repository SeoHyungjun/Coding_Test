#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str, answer;
    int cur = 0, cnt = 0;

    std::cin >> str;

    for (int i = str.length() - 1; i >= 0; --i) {
        if (str[i] == '1') cur += pow(2, cnt);
        cnt += 1;
        
        if (cnt == 3 || i == 0) {
            answer += (cur + '0');
            cnt = 0;
            cur = 0;
        }
    }

    std::reverse(answer.begin(), answer.end());
    std::cout << answer;

    return 0;
}