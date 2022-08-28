#include <iostream>

int main(int argc, char** argv)
{
	int test_case;
	int T;

	std::cin>>T;
	for(test_case = 1; test_case <= T; ++test_case) {
        int sum = 0, num;
        for (int i = 0; i < 10; i++) {
            std::cin >> num;
            sum += num;
        }

        std::cout << "#" << test_case << ' ' << (int)((double)sum/10 +0.5) << '\n';
	}
	return 0;
}