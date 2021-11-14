#include <stdio.h>

int main() {
    int list[5] = {7,2,5,4,1};
    //바깥쪽 for 문에 사용되는 i, 안쪽 for 문에 사용되는 j  //배열 출력을 위해 사용되는 k
    //삽입 정렬 시 key로 사용되는 값을 저장하는 tmp
    int i = 0, j = 0, k = 0, tmp = 0;
    int len = 5; // 배열의 길이 - 1

    for (i = 1; i < len; i++) {
        tmp = list[i];
        for (k = 0; k < len; k++) {
            printf("%d ", list[k]);
        }
        printf("\n");

        for (j = i ; j > 0; j--) {
            //key 값 보다 앞의 값이 작으면 반복을 멈춘다.
            //이때 앞의 값이 작다는 것은 그 앞의 수는 이미 오름차순으로 정렬이 되어있다를 뜻함.
            if (tmp < list[j-1]) {
                list[j] = list[j-1];
                
                for (k = 0; k < len; k++) {
                    printf("%d ", list[k]);
                }
                printf("  tmp = %d\n", tmp);
            }
            else {
                printf("break\n");
                break;
            } 
        }
        list[j] = tmp;
        //j가 마지막으로 있던 위치에 tmp에 저장된 수를 넣는다.

        for (k = 0; k < len; k++) {
            printf("%d ", list[k]);
        }
        printf("\n");
        printf("\n");
    }

    printf("\n");
    for (i = 0; i < len; i++) {
        printf("%d ", list[i]);
    }
    printf("\n");

    return 0;
}