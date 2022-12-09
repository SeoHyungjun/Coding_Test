#include <iostream>
#include <math.h>

using ll = long long;

int N;
ll map[10100];

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::cin >> N;
	for (int i = 0; i < N; ++i) std::cin >> map[i];
	
    ll answer = 0;
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; j++) {
			answer += std::abs(map[i] - map[j]);
		}
	}
	std::cout << answer;
}