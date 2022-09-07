#include <iostream>

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
	int test_case, T, N, M;
    bool flag;

	std::cin >> T;
	for(test_case = 1; test_case <= T; ++test_case) {
        std::cin >> N >> M;
        flag = true;
        while (N--) {
            if (!(M & 1)) {
                flag = false;
                break;
            }
            M >>= 1;
        }
        std::cout << "#" << test_case << ((flag) ? " ON\n" : " OFF\n");
	}
	return 0;
}