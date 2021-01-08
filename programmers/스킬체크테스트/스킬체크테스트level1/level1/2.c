#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(long long int n) {
    int answer = 0;

    while( n != 0 ) {
        answer = answer * 3 + n % 3; 
        n /= 3;
    }

    return answer;
}


int main() {
    printf("%d", solution(45));

    return 0;
}

// 45 % 3 = 15 / 0
// 15 % 3 = 5/ 0
// 5 % 3 = 1 / 2
// 1 % 3 = 0 / 1