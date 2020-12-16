#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(long long int num) {
    int answer = 0;

    while( num != 1 && answer <= 500 ) {
        if (num % 2 == 0) {
            num /= 2;
        }
        else {
            num = num * 3 + 1;
        }
        answer++;
        printf("%d ", num);
    }

    if ( answer > 500 ) return -1;
    else return answer;
}


int main() {
    printf("%d", solution(626331));

    return 0;
}