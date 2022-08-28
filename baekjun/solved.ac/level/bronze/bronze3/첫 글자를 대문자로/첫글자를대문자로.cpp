#include <iostream>
#include <string>
#include <algorithm>

int main() {
    std::ios_base::sync_with_stdio(0);
	std::cin.tie(0), std::cout.tie(0);
    
    int N;
    std::string str;

    std::cin >> N;
    std::cin.ignore();
    
    while (N--) {
        getline(std::cin, str);
        
        if ('a' <= str[0] && str[0] <= 'z') str[0] -= 'a' - 'A';
        std::cout << str << '\n';
    }
    
    return 0;
}