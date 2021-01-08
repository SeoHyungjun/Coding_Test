#include <stdio.h>

int direction[4][4] = { {1, 0}, {0, -1}, {-1, 0}, {0, 1} }; //우, 상, 좌, 하
int plane[101][101] = {0};
int dragon_curve[20][5] = {0};

int find_square() {
    int i = 0, j = 0, k = 0;
    int cnt = 0;

    for(j = 0; j < 101; j++) {
        for(k = 0; k < 101; k++) {
            if( (j + 1 < 101 && k + 1 < 101) && plane[j][k] == 1 && plane[j][k+1] == 1 && plane[j+1][k] == 1 && plane[j+1][k+1] == 1) cnt++;
        }
    }
    return cnt;
}

void make_curve(int N) {
    int i = 0, j = 0, k = 0;
    int tmp_plane[101][101] = {0};
    int line_dir[1024] = {0}; //각 드래곤 커브의 방향을 순서대로 저장
    int cnt = 0; //line_dir에 저장된 데이터의 끝값을 알려주는 값
    int dx = 0, dy = 0;
    int x = 0, y = 0;

    
    //입력된 커브의 갯수만큼 반복
    for (i = 0; i < N; i++) {
        //처음 초기좌표 하나 있으므로 cnt = 1
        line_dir[0] = dragon_curve[i][2];
        cnt = 1;
        
        //커브의 세대만큼 반복하여 이동방향을 저장
        for (j = 0; j < dragon_curve[i][3]; j++) {
            for (k = 0; k <= cnt; k++) {
                line_dir[cnt + k] = (line_dir[cnt  - 1 - k] + 1 ) % 4;
            }
            cnt += cnt;
        }
        /*
        for(k = 0; k < cnt; k++) {
            printf("%d", line_dir[k]);
        }printf("\n");
        */
        //정해진 이동방향을 통해 tmp_plane에 좌표 저장, 1은 커브가 지나갔다는 표시
        x = dragon_curve[i][0];
        y = dragon_curve[i][1];
        tmp_plane[x][y] = 1;
        for (j = 0; j < cnt; j++) {
            dx = direction[ line_dir[j] ][0];
            dy = direction[ line_dir[j] ][1];
            //printf("start = %d %d, next = %d %d, dir = %d\n", x, y, x+dx, y+dy, line_dir[j]);
            if(x+dx >= 0 && x+dx < 101 && y+dy >= 0 &&y + dy < 101 ) tmp_plane[x + dx ][y + dy] = 1;
            x += dx;
            y += dy;
        }
    }
    //tmp_plane의 값을 plane에 복사
    for(i = 0; i < 101; i++){
        for(j = 0; j < 101; j++){
            plane[i][j] = tmp_plane[i][j];
        }
    }
}

int main() {
    int N = 0;
    int i = 0, j = 0;

    scanf("%d", &N);
    
    for(i = 0; i < N; i++) {
        scanf("%d %d %d %d", &dragon_curve[i][0], &dragon_curve[i][1], &dragon_curve[i][2], &dragon_curve[i][3]);
    }
    
    make_curve(N);
    /*
    for(i = 0; i < 101; i++) {
        for (j = 0; j < 101; j++) {
            if(plane[i][j] == 1) printf("%d %d\n", i, j);
        }
    }
    */

    printf("%d", find_square());

    return 0;
}