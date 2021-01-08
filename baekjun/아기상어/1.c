#include <stdio.h>
#include <stdlib.h>

typedef struct shark{
    int x;
    int y;
    int size;
    int eat;
    int move_sec;
} shark;

int main() {
    int i = 0, j = 0, size = 0;
    int **arr = NULL;
    int baby_x = 0, baby_y;
    shark baby_shark;

    //n*n 크기의 배열 생성
    scanf("%d", &size);
    arr = (int**)malloc(sizeof(int*) * size);
    for(i=0; i<size; i++) {
        arr[i] = (int*)malloc(sizeof(int) * size);
        //arr[i][0] = 0; arr[i][1] = 0; arr[i][2] = 0;
    }

    //배열에 맞는 숫자들 입력
    for (i=0; i<size; i++) {
        for(j=0; j<size; j++){
            scanf("%d", &arr[i][j]);
            if(arr[i][j] == 9) {
                baby_shark.x = i;
                baby_shark.y = j;
                baby_shark.eat = 0;
                baby_shark.size = 2;
                baby_shark.move_sec = 0;
            }
        }
    }



    return 0;
}