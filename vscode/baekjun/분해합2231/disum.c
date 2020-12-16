#include <stdio.h>

int main() {
    //입력 변수
    int N; //자연수, 최소 1, 최대 1,000,000

    //결과 값
    int creater = 0; //생성자을 구하여 저장하는 변수
    int dsum = 0; //분해합을 구하여 저장하는 변수

    //반복문에 사용되는 변수
    int i = 0; //반복문 제어
    int tmp = 0; //i의 값을 복사하여 분해합을 계산하기 위해 사용되는 변수

    scanf("%d", &N);

    //1부터 자연수 N-1 까지 분해합을 계산하여, 가장 작은 생성자를 찾는 반복문
    for(i=1; i<N; i++) {
        //i의 값을 복사하여 뒤의 while 문에서 tmp를 나눠가며 분해합 계산
        tmp = i;
        //i의 분해합을 저장하기 위해 매 사이클 마다 초기화 & 분해합의 자기 자신 포함
        dsum = i;
        //i를 사이클마다 10으로 나누어 자리수를 구하면서 나머지값을 tmp에 추가
        while( tmp>0 ) {
            dsum += tmp%10;
            tmp /= 10;
        }

        if( N == dsum) {
            creater = i;
            break;
        }
    }

    printf("%d", creater);

    return 0;
}