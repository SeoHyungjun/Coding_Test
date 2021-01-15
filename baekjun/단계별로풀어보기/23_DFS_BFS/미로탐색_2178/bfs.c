#include <stdio.h>

int map[100][100] = { 0, };
int result[100][100] = { 0, };
int len = 1;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int N = 0, M = 0;

void bfs(int x, int y) {
    int i = 0;
    int x2 = 0, y2 = 0;
    int queue[10000][2] = { 0, };
    int start = 0, end = 0;
    int newx = 0, newy = 0;
    
    queue[end][0] = x;
    queue[end++][1] = y;
    result[x][y] = 1;
    len++;

    while(start < end) {
        x2 = queue[start][0];
        y2 = queue[start++][1];
        //printf("start %d,%d\n", x2, y2);
        /*
        for(i = 0; i < end; i++) {
            printf("%d,%d ", queue[i][0], queue[i][1]);
        }
        printf("\n");
        */

        for(i = 0; i < 4; i++) {
            newx = x2 + dx[i];
            newy = y2 + dy[i];
            //printf("new %d,%d\n", newx, newy);

            if(newx >= 0 && newx < N && newy >= 0 && newy < M && map[newx][newy] == 1 && result[newx][newy] == 0) {
                queue[end][0] = newx;
                queue[end++][1] = newy;
                result[newx][newy] = result[x2][y2] + 1;
            }    
        }
    }
}

int main() {
    int i = 0, j = 0;

    scanf("%d %d", &N, &M);

    for(i = 0; i < N; i++) {
        for(j = 0; j < M; j++) {
            scanf("%1d", &map[i][j]);
        }
    }

    bfs(0, 0);

    /*
    printf("\n");
    for(i = 0; i < N; i++) {
        for(j = 0; j < M; j++) {
            printf("%d", map[i][j]);
        }
        printf("\n");
    }

    printf("\n");
    for(i = 0; i < N; i++) {
        for(j = 0; j < M; j++) {
            printf("%d", result[i][j]);
        }
        printf("\n");
    }
    */
    printf("%d", result[N-1][M-1]);

    return 0;
}