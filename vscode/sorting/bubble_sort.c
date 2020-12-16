#include <stdio.h>
#include <stdlib.h>

int main() {
    int list[5] = {7,5,4,2,1};

    //바깥쪽 for 문에 사용되는 i, 안쪽 for 문에 사용되는 j //배열 출력을 위해 사용되는 k
    //소팅 중 배열의 값 교환을 위해 사용되는 tmp
    int i = 0, j = 0, k = 0, tmp = 0;
    //배열의 길이 len
    int len = 5;

    //버블 소팅 시작
    for (i = 0; i < len - 1; i++) { //
        for (j = 0; j < len - i - 1; j++) {
            //바깥쪽 for 문의 i값에 따라 안쪽 for 문의 반복 횟수가 줄어든다.
            //바깥쪽 for 문의 경우 배열의 길이만큼 반복하게되고
            //안쪽 for 문의 경우에 바깥쪽 for 문의 각 단계마다(오름차순의 경우) 최대값이 맨 뒤로 이동하게되고
            //최대값이 맨 뒤에 존재하므로, 배열의 맨 뒷부분은 다음 단계에서 정렬에 포함되지 않는다.

            //각 단계마다 j의 값에 따라 배열의 j번째 값과 j+1번째 값을 비교
            //만약 j번째 값이 j+1번째 값이 더 크다면 (오름차순 정렬의 경우) 큰 수가 뒤로 가야하므로 배열의 값 교환
            if ( list[j] > list[j+1] ) {
                tmp = list[j];
                list[j] = list[j+1];
                list[j+1] = tmp;
            }
            for (k = 0; k < len; k++) {
                printf("%d ", list[k]);
            }
            printf("\n");
        }
    }
    // n n-1 n-2 n-3
    // 4 3 2 1 
    // bigO( n * (n-1) / 2 ) = bigO( (n^2 - n) / 2 ) = bigO(N^2)

    printf("\n");
    for (i = 0; i < len; i++) {
        printf("%d ", list[i]);
    }
    printf("\n");

    return 0;
}