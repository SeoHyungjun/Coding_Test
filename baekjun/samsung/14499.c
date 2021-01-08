#include <stdio.h>

int map[20][20] = {0};
int dir[1000] = {0}; //1 동 2 서 3 북 4 남
int square[6] = {0};
int x = 0, y = 0;
int dx[5] = {0, 0, 0, -1, 1};
int dy[5] = {0, 1, -1, 0, 0};

void move(int N, int M, int dir) {
    int tmp = 0;int i = 0;

    if(x + dx[dir] >= 0 && x + dx[dir] < N && y + dy[dir] >= 0 && y + dy[dir] < M) {
        x = x + dx[dir];
        y = y + dy[dir];

        if(dir == 1) { //1, 4 고정, 3 *1 0 5 *4 2
            tmp = square[0]; square[0] = square[3]; square[3] = square[5]; square[5] = square[2]; square[2] = tmp;
        }
        else if(dir == 2) { //1, 4 고정, 2 *1 5 0 *4 3
            tmp = square[0]; square[0] = square[2]; square[2] = square[5]; square[5] = square[3]; square[3] = tmp;
        }
        else if(dir == 3) { //2, 3 고정, 4 0 *2 *3 5 1
            tmp = square[0]; square[0] = square[4]; square[4] = square[5]; square[5] = square[1]; square[1] = tmp;
        }
        else if(dir == 4) { //2, 3 고정, 1 5 *2 *3 0 4
            tmp = square[0]; square[0] = square[1]; square[1] = square[5]; square[5] = square[4]; square[4] = tmp;
        }

        if(map[x][y] != 0) {
            square[5] = map[x][y];
            map[x][y] = 0;
        }
        else {
            map[x][y] = square[5];
        }

        /*
        printf("x = %d, y = %d  // ", x, y);
        for(i = 0; i < 6; i++) {
            printf("%d ", square[i]);
        }
        printf("\n");
        */
        
        printf("%d\n", square[0]);
    }
}

int main() {
    int N = 0, M = 0, k = 0;
    int i = 0, j = 0;

    scanf("%d %d %d %d %d", &N, &M, &x, &y, &k);

    for(i = 0; i < N; i++){
        for(j = 0; j < M; j++){
            scanf("%d", &map[i][j]);
        }
    }
    for(i = 0; i < k; i++) {
        scanf("%d", &dir[i]);
    }
    for( i = 0; i < k; i++) {
        move(N, M, dir[i]);
    }

    return 0;
}