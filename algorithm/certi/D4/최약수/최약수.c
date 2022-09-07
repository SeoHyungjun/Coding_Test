#include <stdio.h>

int num_size(int n) {
    int result = 0;
    while (n) {
        ++result;
        n /= 10;
    }
    return result;
}

int cal_head(int n) {
    while (n >= 1000) n /= 10;
    return n;
}

int main(int argc, char** argv) {
	int test_case, T, N, tmp, head;

	scanf("%d", &T);
	for(test_case = 1; test_case <= T; ++test_case) {
        scanf("%d", &N);

        if (N < 2) tmp = 1;
        else if (N < 5) tmp = 2;
        else if (N < 10) tmp = 3;
        else if (N < 20) tmp = 4;
        else if (N < 25) tmp = 5;
        else if (N < 50) tmp = 6;
        else if (N < 100) tmp = 7;
        else {
            tmp = 8 + (num_size(N) - 3) * 5;
            head = cal_head(N);
            if (head >= 500) tmp += 4;
            else if (head >= 250) tmp += 3;
            else if (head >= 200) tmp += 2;
            else if (head >= 125) tmp += 1;
        }
        printf("#%d %d\n", test_case, tmp);
	}
	return 0;
}