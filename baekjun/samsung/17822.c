#include <stdio.h>

int Circle[50][50] = {0};
int Turn[50][3] = {0};
int check[50] = {0};

void delete_circle(int N, int M, int T, int del) {
    int i, j;
    int cnt = 0, sum = 0, avg = 0;
    int check = 0;
    int tmp[50][50] = {0};

    for(i = 0; i<N; i++) {
        for (j = 0; j < M; j++) {
            if(Circle[i][j] != 0 && Circle[i][j] == Circle[i][(j+1)%M]) {
                tmp[i][j] = 1;
                tmp[i][(j+1)%M] = 1;
                check = 1;
            }
            if(i != N && Circle[i][j] != 0 && Circle[i][j] == Circle[i+1][j]){
                tmp[i][j] = 1;
                tmp[i+1][j] = 1;
                check = 1;
            }
            /*
            if (i - 1 >= 0 && j - 1 >= 0) {
                if (Circle[i][j] != 0 && Circle[i][j] == Circle[i-1][j]) {
                    Circle[i][j] = 0;
                    Circle[i-1][j] = 0;
                    check = 1;
                }
                else if (Circle[i][j] != 0 && Circle[i][j] == Circle[i][j-1]) {
                    Circle[i][j] = 0;
                    Circle[i][j-1] = 0;
                    check = 1;
                }
            }
            if(i + 1 < M && j + 1 < M) {
                if(Circle[i][j] != 0 && Circle[i][j] == Circle[i+1][j]) {
                    Circle[i][j] = 0;
                    Circle[i+1][j] = 0;
                    check = 1;
                }
                else if (Circle[i][j] != 0 && Circle[i][j] == Circle[i][j+1]) {
                    Circle[i][j] = 0;
                    Circle[i][j+1] = 0;
                    check = 1;
                }
            }
            */
        }
    }

    for(i = 0; i < N; i++) {
        for(j = 0; j < M; j++) {
            if(tmp[i][j] == 1) Circle[i][j] = 0;
        }
    }

    if(check == 0) {
        sum = 0;
        cnt = 0;
        for (i = 0; i < N; i++ ){
            for(j = 0; j < M; j ++) {
                sum += Circle[i][j];
                if (Circle[i][j] != 0) cnt++;
            }
            
        }
        avg = sum / cnt;

        for(i = 0; i < N; i++){
            for(j = 0; j < M; j++){
                if (sum % cnt == 0) {
                    if(Circle[i][j] > avg && Circle[i][j] != 0) {
                        Circle[i][j] -= 1;
                    }
                    else if(Circle[i][j] < avg && Circle[i][j] != 0) {
                        Circle[i][j] += 1;
                    }
                }
                else {
                    if(Circle[i][j] > avg && Circle[i][j] != 0) {
                        Circle[i][j] -= 1;
                    }
                    else if(Circle[i][j] <= avg && Circle[i][j] != 0) {
                        Circle[i][j] += 1;
                    }
                }
            }
        }
    }

    return;
}

int turn_circle(int A, int B, int T) {
    int result = 0;
    int i, j, k, p, a;
    int tmp[50] = {0};
    int N = A; 
    int M = B;

    //printf("1 %d %d\n", N, M);

    //입력값 T의 줄수 만큼 원판 돌리기
    for (i = 0; i < T; i++) {
        //입력값  T의 줄에서 xi의 배수 원판 돌리기
        for (j = Turn[i][0]; j <= N; j+=Turn[i][0]) {
            //원판 마다 di, ki에 의해 회전, d = 0 시계, d = 1 반시계
            //printf("2 %d %d\n", N, M);
            //시계방향일 경우
            if (Turn[i][1] == 0) {
                for (k = 0; k < M; k++) {
                    //방향에 맞게 한칸씩 옮기기
                    tmp[  (k + Turn[i][2])%M ] = Circle[j - 1][k];
                    //printf("2-1 %d %d\n", N, M);
                }
                for (k = 0; k < M; k++) {
                    Circle[j - 1][k] = tmp[k];
                }
            }
            else {
                for (k = 0; k < M; k++) {
                    //방향에 맞게 한칸씩 옮기기
                    a = k - Turn[i][2];
                    while (a < 0) a = a + M;
                    tmp[ a%M ] = Circle[j - 1][k];
                    //printf("2-2 %d %d\n", N, M);
                }
                for (k = 0; k < M; k++) {
                    Circle[j - 1][k] = tmp[k];
                }
            }
            //printf("3 %d %d\n", N, M);
            //인접한 같은 수 제거
        }
        /*
        for(j = 0; j < N; j++) {
            for( k = 0; k < M; k++) {
                printf("%d ", Circle[j][k]);
            }
            printf("\n");
        }
        */
        delete_circle(N, M, T, i);
        /*
        //printf("4 %d %d\n", N, M);
        for(j = 0; j < N; j++) {
            for( k = 0; k < M; k++) {
                printf("%d ", Circle[j][k]);
            }
            printf("\n");
        }
        printf("\n");printf("\n");
        */

    }

    for(i = 0; i < N; i++) {
        for( j = 0; j < M; j++) {
            result += Circle[i][j];
        }
    }

    return result;
}

int main() {
    int N, M, T;
    int i, j, k;
    int result = 0;

    scanf("%d %d %d", &N, &M, &T);

    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            scanf("%d", &Circle[i][j]);
        }
    }
    for(i = 0; i < T; i++){
        scanf("%d %d %d", &Turn[i][0], &Turn[i][1], &Turn[i][2]);
    }

    result = turn_circle(N, M, T);

    /*
    for(j = 0; j < N; j++) {
        for( k = 0; k < M; k++) {
            printf("%d ", Circle[j][k]);
        }
        printf("\n");
    }
    */
    

    printf("%d", result);

    return 0;
}