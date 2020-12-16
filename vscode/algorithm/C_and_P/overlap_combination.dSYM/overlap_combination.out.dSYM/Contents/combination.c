//조합 알고리즘
//조합은 중복이 불가능
//{1,2}와 {2,1}을 같은것으로 취급
//중복 조합 알고리즘과 다르게 {1,1}과 같이 안의 숫자도 중복 불가능
//C를 사용해서 5C3과 같이 5개중에서 3개를 선택 가능

//index와 target을 인자로 combination 함수를 구현
//index는 com_arr, 3개를 선택해서 저장하는 배열에 위치를 나타냄
//target은 arr, 전체 숫자를 보관하는 배열의 위치를 나타냄
//결국 index,target을 봤을때
//0,0 -> 1저장, 1,1 -> 2저장, 2,2-> 3저장, 3,3 -> index == LEN이므로 저장배열 출력
//index를 하나 낮췄을때 target만 +1해버리면, 1,2가 저장된 상태에서  2,4 -> com_arr의 3번째 위치에 arr의 4번째 위치인 3저장


#include <stdio.h>

#define arr_LEN 3               //전채 숫자의 갯수
#define LEN 2                   //선택할 숫자의 갯수

int arr[arr_LEN] = {1, 2, 3};
int com_arr[LEN] = {0};         //조합을 com_arr에 담아서 확인
int cnt_com = 0;                //총 몇개의 조합이 나왔는지 확인하는 count

void swap(int i, int j) {
    int tmp;

    tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}


void com(int index, int target) {
    int i = 0;

    //if (r == 0) {
    if (index == LEN) {
        for(i = 0; i < LEN; i++) printf("%d ", com_arr[i]);
        printf("\n");
        cnt_com++;
    }
    else if(target == arr_LEN) {
        //printf("else if\n");
        return;
    }

    else { 
        //printf("index = %d, target = %d, arr[target] = %d\n", index, target, arr[target]);
        com_arr[index] = arr[target];
        //printf("com1  ");
        com(index+1, target+1);
        //printf("com2  ");
        com(index, target+1);
    }
}
/*
void com(int index, int cnt) {    //index는 어디 index까지 탐색했는지를 저장하고 그 뒤부터만 사용
    int i = 0;
    printf("%d %d\n", index+1, cnt+1);
    
    if(cnt == LEN ) {
        for(i = 0; i < LEN; i++) {
            printf("%d ", com_arr[i]);
        }
        cnt_com++;
        printf("\n");
        return;
    }
    
    else {
        for(i = index; i < arr_LEN; i++) {
            com_arr[cnt] = arr[i];
            com(index+1, cnt+1);
            com_arr[cnt] = 0;
        }
    }
}
*/

int main() {
    com(0, 0);
    printf("%d", cnt_com);
    return 0;
}