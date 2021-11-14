#include <stdio.h>
#include <stdbool.h>

bool map[1000][1000] = { 0, };
bool check[1000] = { 0, };
bool visit[1001] = { 0, };


void bfs(int N, int M, int V) {
    int i = 0;
    int start = 1, end = 1, cur = 0;
    int queue[1001] = { 0, };

    printf("\n%d ", V);
    visit[V] = 1;
    queue[end++] = V;

    while(start < end) {
        cur = queue[start++];
        //printf("cur = %d\n", cur);

        for(i = 1; i <= N; i++) {
            if(map[cur-1][i-1] == 1 && visit[i] == 0) {
                queue[end++] = i;
                visit[i] = 1;
                printf("%d ", i);
            }
        }
    }
}

void dfs(int N, int M, int V) {
    int i = 0, j = 0;

    printf("%d ", V);
    check[V-1] = 1;
    
    for( i = 1; i <= N; i++) {
        if(map[V-1][i-1] == 1 && check[i-1] == 0 ) {
            dfs(N, M, i);
        }
        else
            continue;
    }
}

int main() {
    int N = 0, M = 0, V = 0;
    int i = 0, j = 0;
    int a = 0, b = 0;

    

    scanf("%d %d %d", &N, &M, &V);

    for(i = 0; i < N; i++) {
        map[i][i] = 1;
    }

    for(i = 0; i < M; i++) {
        scanf("%d %d", &a, &b);
        map[a-1][b-1] = 1;
        map[b-1][a-1] = 1;
    }

    /*
    for(i = 0; i < N; i++) {
        for(j = 0; j < N; j++){
            printf("%d ", map[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    */
    dfs(N, M, V);
    bfs(N, M, V);

    return 0;
}