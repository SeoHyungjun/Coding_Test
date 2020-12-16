#include <stdio.h>

int main() {
    //입력 변수 선언
    int n = 0; //카드의 갯수, 최소 3, 최대 100
    int m = 0; //목표 값, 최소 10, 최대 300,000
    int arr[100] = {'0'};  //카드의 갯수 n 만큼의 수를 입력 받는 배열, 입력 되는 수는 100,000 미만

    //값 저장하는 변수
    int sum = 0;

    //for문에 사용하는 변수
    int i = 0, j = 0, k = 0;

    //카드의 갯수 n과 목표값 m 입력
    scanf("%d %d", &n, &m);        

    //카드에 쓰여있는 수 입력
    for(i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }

    //모든 수를 비교하기 위해 i,j,k를 포함하는 for문에서 3개의 수를 체크
    for(i=0; i<n; i++) {
        for(j=i+1; j<n; j++) {
            for(k=j+1; k<n; k++) {
                //m과 같거나 작으면서, 가장 큰 합을 찾기
                if(arr[i] + arr[j] + arr[k] > sum && arr[i] + arr[j] + arr[k] <= m) {
                    sum = arr[i] + arr[j] + arr[k];
                }
            }
        }
    }

    printf("%d", sum);

    return 0;
}