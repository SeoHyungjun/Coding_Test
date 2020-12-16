#include <stdio.h>

typedef struct virus {
    int x;
    int y;
}virus;

int rap[50][50] = {0};
virus vir[10];
virus start_vir[10];
int vir_cnt = 0;
int min = 2500;
int dir[4][2] = {{0,1}, {0,-1}, {1, 0}, {-1, 0}};

int spread(int N, int M) {
    int i = 0, j = 0, k = 0;
    int tmp_rap[50][50] = {0};
    int tmp_rap2[50][50] = {0};
    int check = 1;
    int check_zero = 1;
    int gen = 0;

    for(i = 0; i < N; i++) {
        for(j = 0; j < N; j++) {
            tmp_rap[i][j] = rap[i][j];
            tmp_rap2[i][j] = rap[i][j];
            if(tmp_rap[i][j] == 0) check_zero = 1;
        }
    }
    if(check_zero == 0) return gen;

    for(i = 0; i < M; i++) {
        tmp_rap[vir[vir_cnt-1-i].x][vir[vir_cnt-1-i].y] = 3;
        tmp_rap2[vir[vir_cnt-1-i].x][vir[vir_cnt-1-i].y] = 3;
    }

    while(1) {
        gen++;
        check = 0;

        for(i = 0; i < N; i++) {
            for(j = 0; j < N; j++) {
                if(tmp_rap[i][j] == 3) {
                    tmp_rap2[i][j] = 3;
                    for(k = 0; k < 4; k++) {
                        if(i+dir[k][0] >= 0 && i+dir[k][0] < N && j+dir[k][1] >= 0 && j+dir[k][1] < N && (tmp_rap[i+dir[k][0]][j+dir[k][1]] == 0 || tmp_rap[i+dir[k][0]][j+dir[k][1]] == 2)) {
                            tmp_rap2[i+dir[k][0]][j+dir[k][1]] = 3;
                            check = 1;
                        }
                    }
                }
            }
        }

        check_zero = 0;
        //printf("gen = %d\n", gen);
        for(i = 0; i < N; i++) {
            for(j = 0; j<N; j++) {
                if(tmp_rap2[i][j] == 3) tmp_rap[i][j] = tmp_rap2[i][j];
                //printf("%d", tmp_rap[i][j]);
                if(tmp_rap[i][j] == 0) check_zero = 1;
            }
            //printf("\n");
        }
        //printf("\n");

        if(check == 0 && check_zero == 1) {
            return -1;
        }

        else if(check_zero == 0) {
            return gen;
        }

        if(gen > min) return -1;
    }
    return gen;
}

void print_vir(int M, int cnt) {
    int i = 0;
    printf("%d\n", cnt);
    for(i = 0; i < 10; i++) {
        printf("%d %d / ", vir[i].x, vir[i].y);
    }
    printf("\n");
}

void swap(i, j){
    virus tmp;

    tmp.x = vir[i].x; tmp.y = vir[i].y;
    vir[i].x = vir[j].x; vir[i].y = vir[j].y;
    vir[j].x = tmp.x; vir[j].y = tmp.y;
}

void select_virus(int N, int M, int cnt) {
    int i = 0, j = 0;
    int result = 0;

    if ( cnt == M ) {
        //print_vir(M, cnt);
        result = spread(N, M);
        if (result < min && result != -1) min = result;
        return;
    }

    for(i = 0; i < vir_cnt-cnt; i++) {
        swap(i, vir_cnt-1-cnt);
        //print_vir(M, cnt);
        select_virus(N, M, cnt+1);
        swap(i, vir_cnt-1-cnt);
        //print_vir(M, cnt);
    }
}

void find_result(int N, int M) {
    int i = 0, j = 0;
    int start = 0;
    int cnt = 0;
    int result = 0;
    int first = 0;

    select_virus(N, M, 0);
}

int main() {
    int N = 0, M = 0;
    int i = 0, j = 0;

    scanf("%d %d", &N, &M);

    for(i = 0; i < N; i++) {
        for(j = 0; j < N; j++) {
            scanf("%d", &rap[i][j]);

            if(rap[i][j] == 2) {
                vir[vir_cnt].x = i;
                vir[vir_cnt++].y = j;
            }
        }
    }

    find_result(N, M);
    if(min != 2500 )printf("%d", min);
    else printf("-1");

    return 0;
}