#include <stdio.h>
#include <string.h>

int map[26][26] = { 0, };
int group[26][26] = { 0, };
int visit[26][26] = { 0, };
int result[625] = { 0, };

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int N = 0;
int group_cnt = 1;
int in_group_cnt = 0;
int result_cnt = 0;

void dfs(int x, int y) {
    int i = 0, j = 0;
    

    //printf("%d,%d ] ", x, y);
    visit[x][y] = 1;
    group[x][y] = group_cnt;
    in_group_cnt++;

    for(i = 0; i < 4; i++){
        //printf("%d,%d ", x + dx[i], y + dy[i]);
        if(x + dx[i] > 0 && x + dx[i] <= N && y + dy[i] > 0 && y + dy[i] <= N && visit[x + dx[i]][y + dy[i]] == 0 && map[x + dx[i]][y + dy[i]] == 1) {
            //printf("ok\n");
            dfs(x + dx[i], y + dy[i]);
        }
    }
}

int main() {
    char a[26] = { '\0', };
    int i = 0, j = 0;

    scanf("%d", &N);
    getchar();

    for(i = 1; i <= N; i++) {
        scanf("%s", &a);
        for(j = 0; j < N; j++) { 
            if(a[j] == '0') map[i][j+1] = 0;
            else if(a[j] == '1') map[i][j+1] = 1;
        }
    }

/*
    printf("\n");
    for(i = 1; i <= N; i++) {
        for(j = 1; j <= N; j++) {
            printf("%d", map[i][j]);
        }
        printf("\n");
    }
*/
    for(i = 1; i <= N; i++) {
        for(j = 1; j <= N; j++) {
            if( map[i][j] == 1 && group[i][j] == 0) {
                in_group_cnt = 0;
                dfs(i, j);
                group_cnt++;
                result[result_cnt++] = in_group_cnt;
            }
        }
    }
/*
    printf("\n");
    for(i = 1; i <= N; i++) {
        for(j = 1; j <= N; j++) {
            printf("%d", group[i][j]);
        }
        printf("\n");
    }
*/
    printf("%d\n", group_cnt - 1);
    for(i = 0; i < group_cnt - 1; i++) {
        printf("%d\n", result[i]);
    }

    return 0;
}