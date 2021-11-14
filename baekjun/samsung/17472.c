#include <stdio.h>

typedef struct island {
    int x;
    int y;
}island;

int map[10][10] = {0};
island start_island[6];
int num_island = 0;
int marking = 2;
int bri[6][6] = {0};
int connected[6] = {0};
int test[120] = {0};
int cnt = 0;
int arr[120] = {0};
int total_min = 60;

int sum_arr() {
    int i = 0;
    int sum = 0;

    for(i = 0; i < marking - 2; i++) {
        sum += arr[i];
    }

    return sum;
}

void cal(int index, int target) {
    int i = 0;
    int sum = 0;

    if(index == marking - 2 - 1) {
        sum = sum_arr();
        if( sum < total_min )  total_min = sum;
    }
    else if(target == cnt) return;
    else {
        arr[index] = test[target];
        cal(index + 1, target + 1);
        cal(index, target + 1);
    }
}

int change_island(int N, int M, int x, int y) {
    if(map[x][y] == 1) {
        map[x][y] = marking;
    
        if(map[x+1][y] == 1 && x+1 < N) change_island(N, M, x+1, y);
        if(map[x][y+1] == 1 && y+1 < M) change_island(N, M, x, y+1);
        if(map[x-1][y] == 1 && x-1 >= 0) change_island(N, M, x-1, y);
        if(map[x][y-1] == 1 && y-1 >= 0) change_island(N, M, x, y-1);

        return 0;
    }
    else return 1;
}

int main() {
    int N = 0, M = 0;
    int i = 0, j = 0, k = 0;
    int re = 0;
    int len = 0, dest = 0;
    int min = 0;
    int max = 0;
    int sum = 0;
    int result = 0;

    scanf("%d %d", &N, &M);
    for(i = 0; i < N; i++) {
        for(j = 0; j < M; j++) {
            scanf("%d", &map[i][j]);
            if(  (i == 0 || map[i-1][j] == 0) && (j == 0 || map[i][j-1] == 0) && map[i][j] == 1) {
                start_island[num_island].x = i;
                start_island[num_island].y = j;
                num_island++;
            }
        }
    }

    for(i=0; i<num_island; i++) {
        //printf("for %d\n", i);
        if (change_island(N, M, start_island[i].x, start_island[i].y) == 0) marking++;
    }

    /*
    for(i = 0; i < N; i++) {
        for(j = 0; j < M; j++) {
            printf("%d ", map[i][j]);
        }
        printf("\n");
    }
    */

    //printf("marking = %d\n", marking);

    for(i = 0; i < N; i++) {
        for(j = 0; j < M; j++) {
            if(map[i][j] != 0 && map[i][j+1] == 0 && j+1 < M) {
                len = 0;
                dest = 0;
                for(k = j+1; k < M; k++){
                    if(map[i][k] == 0) len++;
                    else {
                        dest = map[i][k];
                        break;
                    }
                }
                //printf("len = %d, start = %d,%d, dest = %d\n", len, i,j, dest);
                if(dest != 0 && len >= 2 && (len < bri[map[i][j]][dest] || bri[map[i][j]][dest] == 0 )){
                    //printf("in len = %d, x,y = %d,%d, start = %d, dest = %d\n", len, i,j, map[i][j], dest);
                    bri[map[i][j]-2][dest-2] = len;
                    bri[dest-2][map[i][j]-2] = len;
                }
            }
            if(map[i][j] != 0 && map[i+1][j] == 0 && i+1 < M) {
                len = 0;
                dest = 0;
                for(k = i+1; k < N; k++){
                    if(map[k][j] == 0) len++;
                    else {
                        dest = map[k][j];
                        break;
                    }
                }
                //printf("len = %d, start = %d,%d, dest = %d\n", len, i,j, dest);
                if(dest != 0 && len >= 2 && (len < bri[map[i][j]][dest] || bri[map[i][j]][dest] == 0 )){
                    //printf("in len = %d, x,y = %d,%d, start = %d, dest = %d\n", len, i,j, map[i][j], dest);
                    bri[map[i][j]-2][dest-2] = len;
                    bri[dest-2][map[i][j]-2] = len;
                }
            }
        }
    }

    
    for(i = 0; i < marking-2; i ++){
        for(j = 0; j < marking-2; j++) {
            printf("%d ", bri[i][j]);
            if(i != j) min += bri[i][j];
        }
        printf("\n");
    }
    

    for(i = 1; i < marking-2; i++) {
        for(j = 0; j < i; j++) {
            //printf("%d ", bri[i][j]);
            if(bri[i][j] != 0) {
                test[cnt] = bri[i][j];
                sum += bri[i][j];
                cnt++;
                if(max < bri[i][j]) max = bri[i][j];
            }
        }
        //printf("\n");
    }

    if(cnt < marking - 2 -1){
        total_min = -1;
    }
    else 
        cal(0, 0);

    /*
    if(cnt == marking-2) {
        printf("%d", sum - max);
    }
    else if(cnt == marking - 3){
        printf("%d", sum);
    }
    else {
        printf("-1");
    }
    */
    if(total_min != 60 )
        printf("%d", total_min);
    else
        printf("-1");

    return 0;
}