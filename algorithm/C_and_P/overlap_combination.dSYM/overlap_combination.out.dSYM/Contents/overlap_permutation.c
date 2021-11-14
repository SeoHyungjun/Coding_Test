//중복 순열 알고리즘
//순열은 중복 가능, 조합은 중복이 불가능
//{1,2}와 {2,1}을 다른것으로 취급 (왜? 순서가 다르니까)
//그리고 중복 순열의 경우 {1,1}과 같이 안의 숫자는 중복 가능
//결국 dfs와 같은 알고리즘이 아닌지?(전체 탐색이므로...?)
//길이 4인 배열의 중복 조합 전체 갯수는 256개 == 4^4
//길이 3인 배열의 중복 조합 전체 갯수는 27개 == 3^3

#include <stdio.h>

#define arr_LEN 3
#define LEN 2

int arr[arr_LEN] = {1, 2, 3};
int com_arr[LEN] = {0};         //조합을 com_arr에 담아서 확인
int cnt_com = 0;                //총 몇개의 조합이 나왔는지 확인하는 count

void o_com(int cnt) {
    int i = 0;
    
    if(cnt == LEN) {
        for(i = 0; i < LEN; i++) {
            printf("%d ", com_arr[i]);
        }
        cnt_com++;
        printf("\n");
        return;
    }
    
    else {
        for(i = 0; i < arr_LEN; i++) {
            com_arr[cnt] = arr[i];
            o_com(cnt+1);
            com_arr[cnt] = 0;
        }
    }

}

int main() {
    o_com(0);
    printf("%d", cnt_com);
    return 0;
}