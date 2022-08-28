#include <iostream>
#include <string>
#include <algorithm>

int main() {
    std::ios_base::sync_with_stdio(0);
	std::cin.tie(0), std::cout.tie(0);
    
    std::string str;
    int answer = 1;

    std::cin >> str;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == ',') answer++;
    }

    std::cout << answer;
    
    return 0;
}