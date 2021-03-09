#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
int solution(int arr[], size_t arr_len) {
    int answer = 1;
    int i = 0, j = 0;

    /*
    for(i = 0; i < arr_len; i++) {
        printf("%d ", arr[i]);
    }printf("\n");
    */
    for(i = 0; i < arr_len; i++) {
        for(j = 0; j < arr_len; j++) {
            if (i != j) {
                //printf("%d / %d  = %d\n", arr[j], arr[i], arr[j]%arr[i]);
                if ( arr[i] < arr[j] && arr[j] % arr[i] == 0) {
                    //printf(" in\n");
                    arr[j] = arr[j] / arr[i];
                }
            }
        }
    }
    /*
    for(i = 0; i < arr_len; i++) {
        printf("%d ", arr[i]);
    }printf("\n");
    */
    for(i = 0; i < arr_len; i++) {
        answer *= arr[i];
    }

    return answer;
}

int main() {
    int arr[] = {2,6,8,14};
    printf("%d", solution(arr, 4));

    return 0;
}