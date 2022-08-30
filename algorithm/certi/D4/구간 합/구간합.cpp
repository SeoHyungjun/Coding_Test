#include <iostream>
#include <string.h>

long long int answer[10];

void calculate(long long int num, long long int increase) {
    while (num) {
        answer[num % 10] += increase;
        num /= 10;
    }
}

void func(long long int start, long long int end, long long int placeOfNum) {
    if (start == 0) start = 1;
    while (start <= end) {
        while (start % 10 != 0 && start <= end) {
            calculate(start, placeOfNum);
            ++start;
        }

        if (end < start) break;

        while (end % 10 != 9 && start <= end) {
            calculate(end, placeOfNum);
            --end;
        }

        start /= 10;
        end /= 10;

        for (int i = 0; i < 10; ++i) answer[i] += (end - start + 1) * placeOfNum;
        placeOfNum *= 10;
    }
}

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
	int test_case, T;
    long long int a, b;

	//freopen("input.txt", "r", stdin);
	std::cin>>T;
	for(test_case = 1; test_case <= T; ++test_case) {
        memset(answer, 0, sizeof(long long int)*10);
        std::cin >> a >> b;
        func(a, b, 1);
        long long int sum = 0;
        for (int i = 0; i < 10; ++i) sum += answer[i]*i;
        std::cout << '#' << std::to_string(test_case) << ' ' << std::to_string(sum) << '\n';
	}

	return 0;
}