#include <stdio.h>

int main(void) {
	int test_case, T, answer;
    long long int K;
	setbuf(stdout, NULL);
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case) {
        scanf("%lld", &K);
        --K;
        
        while (K & 1) K = (K-1)/2;
        if (K % 4 == 0) answer = 0;
        else answer = 1;

        printf("#%d %d\n", test_case, answer);
	}

	return 0;
}


/*
p0 = 0
p1 = p0 + 0 + f(g(p0)) = 0 + 0 + !0 = 001
p2 = p1 + 0 + f(g(p1)) = 001 + 0 + !100 = 001 + 0 + 011 = 0010011
p3 = p2 + 0 + f(g(p2)) = 0010011 + 0 + !1100100 = 0010011 + 0 + 0011011 = 001001100011011
p4 = p3 + 0 + f(g(p3)) = 001001100011011 + 0 + !110110001100100 = 001001100011011 + 0 + 001001110011011 = 0010011000110110001001110011011

index of 1
p4 = [2 5 6 10 11 13 14 18 21 22 23 26 27 29 30]
index of 0
p4 = [0 1 3 4 7 8 9 12 15 16 17 19 20 24 25 28]
*/