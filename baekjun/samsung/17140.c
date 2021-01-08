#include <stdio.h>
int A[101][101] ={0};
int row = 3, col = 3;

int R_cal();
int C_cal();
int Find_k(int, int, int);

int main() {
    int r = 0, c = 0, k = 0;
    int i = 0, j = 0;
    int result = 0;

    scanf("%d %d %d", &r, &c, &k);

    for(i = 0; i < 3; i++) {
        scanf("%d %d %d", &A[i][0], &A[i][1], &A[i][2] );
    }
    printf("\n");

    result = Find_k(r, c, k);

    printf("%d", result);

    return 0;
}

int R_cal() {
    int i = 0, j = 0, k = 0;
    int min = 0, col_cnt = 0, col_max = col;
    int tmp_ten[10] = {0}; //각 index가 숫자, 안에는 반복횟수 저장
    int B[101] = {0};

    for(i = 0; i < row; i++) {
        //tmp 초기화
        for (j = 0; j < 10; j++) {
            tmp_ten[j] = 0;
        }
        for (j = 0; j < col_max; j++) {
            B[j] = 0;
        }
        min = 0;

        // 각 row의 숫자별 갯수 저장
        for (j = 0; j < col; j++) {
            tmp_ten[ A[i][j] ]++;
        }

        /*
        //row의 가장 적게 중복된 수 확인
        for (j = 1; j < 10; j++) {
            if( j == 1 ) min = tmp_ten[j];
            else {
                if( tmp_ten[j] < min && tmp_ten[j] != 0 ) min = tmp_ten[j];
            }
        }
        */

        min = 1;
        col_cnt = 0;
        //row의 가장 작은 중복횟수부터, row의 맨 앞부터 찾으면서 B배열에 저장
        for (j = 1; j < 10; j++) {
            //작은 숫자부터 적은 중복횟수 저장
            for (k = 1; k < 10; k++) {
                if ( tmp_ten[k] == min ) {
                    B[col_cnt++] = k;
                    B[col_cnt++] = min;
                    tmp_ten[k] = 0;
                }
            }
            min++;
        }
        
        if (i == 0 ) {
            col_max = col_cnt;
        }
        else {
            if (col_cnt >= col_max) col_max = col_cnt;
        }
        for(j = 0; j < col_max; j++){
            A[i][j] = B[j];
        }
    }

    col = col_max;

    return 0;
}

int C_cal() {
    int i = 0, j = 0, k = 0;
    int min = 0, row_cnt = 0, row_max = row;
    int tmp_ten[10] = {0}; //각 index가 숫자, 안에는 반복횟수 저장
    int B[101] = {0};

    for(i = 0; i < col; i++) {
        //tmp 초기화
        for (j = 0; j < 10; j++) {
            tmp_ten[j] = 0;
        }
        for (j = 0; j < row_max; j++) {
            B[j] = 0;
        }
        min = 0;

        // 각 row의 숫자별 갯수 저장
        for (j = 0; j < row; j++) {
            tmp_ten[ A[j][i] ]++;
        }

        min = 1;
        row_cnt = 0;
        //row의 가장 작은 중복횟수부터, row의 맨 앞부터 찾으면서 B배열에 저장
        for (j = 1; j < 10; j++) {
            //작은 숫자부터 적은 중복횟수 저장
            for (k = 1; k < 10; k++) {
                if ( tmp_ten[k] == min ) {
                    B[row_cnt++] = k;
                    B[row_cnt++] = min;
                    tmp_ten[k] = 0;
                }
            }
            min++;
        }
        if (i == 0 ) {
            row_max = row_cnt;
        }
        else {
            if (row_cnt >= row_max) row_max = row_cnt;
        }
        for(j = 0; j < row_max; j++){
            A[j][i] = B[j];
        }
    }

    row = row_max;

    return 0;
}

int Find_k(int r, int c, int k) {
    int i = 0, j = 0;
    int cnt = 0;

    while ( A[r-1][c-1] != k ) {
        if ( row >= col ) {
            printf("R_cal\n");
            R_cal();
        }
        else {
            printf("C_cal\n");
            C_cal();
        }

        if (cnt < 10) {
            for(i = 0; i < row; i++) {
                for(j = 0; j < col; j++) {
                    printf("%d ",A[i][j]);
                }
                printf("\n");
            }
            printf("\n");
        }

        cnt++;
        if(cnt > 100) return -1;
    }

    return cnt;
}