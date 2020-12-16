#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct data {
    int size;
    int num;
} data;

char ***result;
char numarr[10][5][3] = {
    { {'#', '#', '#'}, {'#', '.', '#'}, {'#', '.', '#'}, {'#', '.', '#'}, {'#', '#', '#'} },
    { {'.', '.', '#'}, {'.', '.', '#'}, {'.', '.', '#'}, {'.', '.', '#'}, {'.', '.', '#'} },
    { {'#', '#', '#'}, {'.', '.', '#'}, {'#', '#', '#'}, {'#', '.', '.'}, {'#', '#', '#'} },
    { {'#', '#', '#'}, {'.', '.', '#'}, {'#', '#', '#'}, {'.', '.', '#'}, {'#', '#', '#'} },
    { {'#', '.', '#'}, {'#', '.', '#'}, {'#', '#', '#'}, {'.', '.', '#'}, {'.', '.', '#'} },

    { {'#', '#', '#'}, {'#', '.', '.'}, {'#', '#', '#'}, {'.', '.', '#'}, {'#', '#', '#'} },
    { {'#', '.', '.'}, {'#', '.', '.'}, {'#', '#', '#'}, {'#', '.', '#'}, {'#', '#', '#'} },
    { {'#', '#', '#'}, {'.', '.', '#'}, {'.', '.', '#'}, {'.', '.', '#'}, {'.', '.', '#'} },
    { {'#', '#', '#'}, {'#', '.', '#'}, {'#', '#', '#'}, {'#', '.', '#'}, {'#', '#', '#'} },
    { {'#', '#', '#'}, {'#', '.', '#'}, {'#', '#', '#'}, {'.', '.', '#'}, {'.', '.', '#'} }
};

int main() {
    int N; // 0< N < 100

    char str[10]; //TOP, MIDDLE, BOTTOM;

    int i = 0, j = 0, k = 0, p = 0;

    data *inputdata;

    int datacount = 0;
    int datanum = 0; 
    int max = 0;
    int tmp = 0;
    int checkdata = 0;

    scanf("%d %s", &N, str);
    //getchar();
    inputdata = (data*)malloc( sizeof(data) * N );

    for (i = 0; i < N; i++) {
        tmp = 0;
        scanf("%d %d", &inputdata[i].size, &inputdata[i].num);
        if (inputdata[i].size > max) max = inputdata[i].size;
        tmp = inputdata[i].num;
        while(tmp > 0){
            datanum+=1;
            tmp/=10;
        }
    }

    result = (char***)malloc(sizeof(char**) * datanum);
    for(i = 0; i<datanum; i++) {
        result[i] = (char**)malloc( sizeof(char*) * (2*max - 1) );
        for(j = 0; j < 2*max-1; j++) {
            result[i][j] = (char*)malloc(sizeof(char)*max);
            for(k = 0; k < max; k++){
                result[i][j][k] = '.';
            }
        }
    }

    for(p = 0; p < N; p++) {
        tmp = inputdata[i].num;
        while(tmp > 0) {
            checkdata = tmp%10;

            printf("2");
            for(i = 0; i < 2*max -1 ; i++) {
                for(j = 0; j < max; j++) {
                    if( i == 0 || i == 2*max - 2 || i == (2*max-1)/2 + 1 ) {
                        if( j == 0 || j == max - 1) {
                            result[p][i][j] = numarr[checkdata][0][0]
                        }
                    }
                    else {

                    }
                }
            }

            datacount++;
            tmp/=10;
        }

    }
    /*
    for (i = 0; i < N; i++) {
        printf("%d %d\n", inputdata[i].num, inputdata[i].size);
    }
    */


    for (i = 0; i < 2*max-1; i++) { //2
        for (j = 0; j < datanum; j++) { //1
            for(k = 0; k < max; k++) { //3
                printf("%c", result[j][i][k]);
            }
            printf(" ");
        }
        printf("\n");
    }

    for(i = 0; i<datanum; i++) {
        for(j = 0; j < 2*max-1; j++) {
            free(result[i][j]);
        }
        free(result[i]);
    }
    free(result);

    return 0;
}