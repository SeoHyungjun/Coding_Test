#include <stdio.h>

int main() {
    int arr[5] = {4, 1, 7, 2, 5};
    //범위 내에서 가장 작은 값의 인덱스를 저장하기 위해서 min사용, 배열의 원소 교환 시 tmp에 저장해서 교환
    int min, tmp;
    //for문에 사용되는 i,j     //배열 출력을 위해 사용되는 k
    //i는 바깥쪽 for 문에 사용되며, 정렬되지 않은 범위를 뜻함..
    //j는 정렬되지 않은 범위(i의 값)부터 배열의 마지막까지 반복
    int i = 0, j = 0, k = 0; 

    for ( k = 0; k < 5; k++ ) {
        printf("%d ", arr[k]);
    }
    printf("\n\n");

    //sizrof(arr)하면 5가아니라 20, 즉 배열의 byte가 나옴. 
    //int는 4byte니까 20/4하면 5개의 원소를 갖는 배열이라는 것을 알 수 있음
    //마지막 한 개의 원소만 남았을 경우 비교할 필요가 없으므로 5-1까지만 실행
    for ( i = 0; i < (int)sizeof(arr)/4 - 1; i++ ) {
        //가장 작은 수를 맨 앞부터 비교하기 때문에 맨 처음에 가장 작은수는 i라고 볼 수 있음
        min = i;
        //첫 i의 for문이 끝나면 맨 앞의 원소는 정렬되었다고 볼 수 있으므로 다음 for문에서는 2번째 원소부터 탐색하면 됨 
        //맨 첫번째 수는 min으로 설정되어 있으므로 범위의 2번째 수부터 비교하면 되므로 j = i + 1
        for ( j = i + 1; j < (int)sizeof(arr)/4; j++ ) {
            //범위 내의 수가 min보다 작은지 확인하고, 작다면 그 수의 인덱스를 저장
            //printf("%d\n", j);
            if( arr[j] < arr[min] ) {
                min = j;
            }
        }
        //범위 내에서 가장 작은 수를 찾았으므로 범위의 가장 왼쪽 원소와 가장 작은 원소를 교환
        if( min != i ) {
            tmp = arr[i];
            arr[i] = arr[min];
            arr[min] = tmp;
        }

        for ( k = 0; k < 5; k++ ) {
            printf("%d ", arr[k]);
        }
        printf("\n");
    }

    return 0;
}