#include <stdio.h>

#define N 5
#define R 3

int arr[N] = {1, 2, 3, 4, 5};
int output_arr[R] = {0};

void com(int index, int target) {
    int i = 0;
    if(index == R) {
        for(i = 0; i < R; i++){
            printf("%d ", output_arr[i]);
        }
        printf("\n");
    }
    else if(target == N) {

    }
    else {
        output_arr[index] = arr[target];
        com(index+1, target+1);
        com(index, target+1);
    }
}

int main() {
    com(0,0);

    return 0;
}