#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, K;

    std::cin >> N >> K;

	if (N <= K) {
		std::cout << 0 << "\n";
		return 0;
	}

	int result;

	for (result = 0; ;result++) {
		int cnt = 0;
		int tempN = N;

		while (tempN) {
			if (tempN % 2) ++cnt;
			tempN /= 2;
		}

		if (cnt <= K) break;
		++N;
	}

	std::cout << result << "\n";

    return 0;
}