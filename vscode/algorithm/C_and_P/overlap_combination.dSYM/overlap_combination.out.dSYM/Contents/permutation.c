#include <stdio.h>

#define arr_LEN 3
#define LEN 2

int arr[arr_LEN] = {1, 2, 3};
int com_arr[LEN] = {0};

void swap(int i, int j) {
    int tmp = 0;

    tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}

void per(int cnt) {
    int i = 0;

    if(cnt == LEN) {
        for(i = 0; i < LEN; i++) {
            printf("%d ", arr[i]);
        }
        printf("\n");
    }
    else {
        for(i = cnt; i < arr_LEN; i++) {
            swap(i, cnt);
            per(cnt + 1);
            swap(i, cnt);
        }
    }
}

int main() {

    per(0);

    return 0;
}