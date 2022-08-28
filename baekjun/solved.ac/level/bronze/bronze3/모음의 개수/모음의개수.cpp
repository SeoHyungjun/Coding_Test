#include <iostream>
#include <string>
#include <algorithm>

int main() {
    std::ios_base::sync_with_stdio(0);
	std::cin.tie(0), std::cout.tie(0);
    
    std::string word;
    int answer = 0;

    std::cin >> word;
    for (int i = 0; i < word.length(); i++) {
        if (word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u') answer++;
    }

    std::cout << answer;
    
    return 0;
}