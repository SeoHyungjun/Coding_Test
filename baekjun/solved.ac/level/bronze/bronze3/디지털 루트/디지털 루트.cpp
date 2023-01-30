#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string str;
	int sum;

	while (true) {
		sum = 0;
		std::cin >> str;
		if (str == "0") break;

		while(1) {
			for(int i = 0; i < str.length(); ++i) sum += str[i] - '0';
			if (sum < 10) break;
            str = std::to_string(sum);
            sum = 0;
		}

		std::cout << sum << '\n';
	}

    return 0;
}