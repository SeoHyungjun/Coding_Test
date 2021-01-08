#include <stdio.h>

int map[101][101] = { 0, };
int visit[101] = { 0, };

int computer_num = 0;
int connection = 0;
int result = -1;

void dfs(int start) {
    int i = 0;

    //printf("%d ", start);
    result++;
    visit[start] = 1;

    for(i = 1; i <= computer_num; i++) {
        if( map[start][i] == 1 && visit[i] == 0) {
            dfs(i);
        }
        else{
            continue;
        }
        
    }
}

int main() {
    int com_a = 0, com_b = 0;
    int i = 0, j = 0;


    scanf("%d", &computer_num);
    scanf("%d", &connection);

    for(i = 0; i < connection; i++) {
        scanf("%d %d", &com_a, &com_b);
        map[com_a][com_b] = map[com_b][com_a] = 1;
    }

    /*
    for(i = 1; i <= computer_num; i++) {
        for(j = 1; j <= computer_num; j++) {
            printf("%d ", map[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    */

    dfs(1);
    printf("%d", result);


    return 0;
}