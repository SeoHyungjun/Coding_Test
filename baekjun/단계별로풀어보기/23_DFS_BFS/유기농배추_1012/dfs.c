#include <stdio.h>

int map[50][50] = { 0, };
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int T = 0, M = 0, N = 0, K = 0;
int group_cnt = 1; //실제는 -2하면됨

void dfs(int x, int y) {
    int i = 0;

    map[x][y] = group_cnt;
    for(i = 0; i < 4; i++) {
        if(x + dx[i] >= 0 && x + dx[i] < N && y + dy[i] >= 0 && y + dy[i] < M && map[x+dx[i]][y+dy[i]] == 1) {
            dfs(x+dx[i], y+dy[i]);
        }
    }
}

int main() {
    int X = 0, Y = 0;
    int i = 0, j = 0, r = 0;


    scanf("%d", &T);

    for(i = 0; i < T; i++) {
        scanf("%d %d %d", &M, &N, &K);
        
        for(j = 0; j < 50; j++) {
            for(r = 0; r < 50; r++) {
                map[j][r] = 0;
            }
        }

        for(j = 0; j < K; j++) {
            scanf("%d %d", &X, &Y);
            map[Y][X] = 1;
        }

        group_cnt = 1;
        for(j = 0; j < N; j++) {
            for(r = 0; r < M; r++) {
                if(map[j][r] == 1) {
                    group_cnt++;
                    dfs(j, r);
                }
            }
        }
        printf("%d\n", group_cnt - 1);
    }
    return 0;
}