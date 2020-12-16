#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// nums_len은 배열 nums의 길이입니다.
int solution(int nums[], size_t nums_len) {
    int answer = 0;
    int i = 0, j = 0, k = 0, n = 0, m = 0;
    int com[3] = {0,};
    int sum = 0;
    int check = 0;

    for(i = 0; i < nums_len - 2; i++) {
        com[0] = nums[i];
        sum += com[0];
        for(j = i+1; j < nums_len - 1; j++) {
            com[1] = nums[j];
            sum += com[1];
            for( k = j+1; k < nums_len; k++) {
                com[2] = nums[k];
                sum += com[2];
                
                //소수 계산
                for(m = 2; m < sum; m++) {
                    //printf("%d / %d = %d\n", sum, m, sum%m);
                    if(sum % m == 0) {
                        check = 1;
                        break;
                    }
                }
                if (check == 0) answer++;
                check = 0;
                sum -= com[2];
            }
            sum -= com[1];
        }
        sum -= com[0];
    } 


    return answer;
}


int main() {
    int nums[] = {1, 2, 3, 4};
    printf("%d", solution(nums, 4));

    return 0;
}