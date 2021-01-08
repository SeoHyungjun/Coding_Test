#include <stdio.h>
#include <string.h>
#include <stdlib.h>


typedef struct data {
    int weight;
    int height;
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
    int N = 0;
    char str[10];
    data *input_data;

    int input_num_total_len = 0;
    int input_num_len = 0;
    int input_num_tmp = 0;
    
    int input_height_max = 0;

    int i = 0, j = 0, k = 0;


    // 첫번째 줄 입력, N과 정렬 위치 입력
    scanf("%d %s", &N, str);
    //getchar();

    // 두번째 줄 부터 들어오는 입력

    //두번째 줄 부터 끝까지 들어오는 데이터를 data 구조체에 저장하기 위해 동적 할당
    input_data = (data*)malloc(sizeof(data) * N);
    //두번째 줄 부터 끝까지 들어오는 데이터를 저장
    for ( i = 0; i < N; i++ ) {
        scanf("%d %d", &input_data[i].weight, &input_data[i].num);
        //입력받은 값 중 weight를 통해 height 계산하여 저장
        input_data[i].height = 2*input_data[i].weight - 1;

        // 세로(height)의 길이 중 가장 큰 값을 계산하여 저장
        if(input_data[i].height > input_height_max) {
            input_height_max = input_data[i].height;
        }

        // 마지막으로 출력해야 할 문자의 개수를 계산하여 저장
        input_num_tmp = input_data[i].num;
        while(input_num_tmp > 0) {
            input_num_total_len += 1;
            input_num_tmp /= 10;
        }
    }
    printf("total len = %d\n", input_num_total_len);
    //sleep(5);
    printf("0");
    //결과 값에 저장 될 문자의 크기를 알았으므로 result 동적 할당
    //3차원 배열 중 가장 앞, 숫자의 갯수를 나타냄
    result = (char***)malloc(sizeof(char**) * input_num_total_len);
    printf("1");
    //3차원 배열 중 두번째, 숫자의 높이를 나타냄. 높이는 input_data에 저장된 height를 기준으로 설정
    for(i = 0; i < input_num_total_len; i++) {
        result[i] = (char**)malloc(sizeof(char*) * input_data[i].height);
        printf("2");
        // 3차원 배열 중 마지막, 숫자의 넓이를 나타냄. 넓이는 input_data에 저장된 weight를 기준으로 설정
        for(j = 0; j < input_data[i].height; j++) {
            result[i][j] = (char*)malloc(sizeof(char) * input_data[i].weight);
            printf("3");
            // 3차원 배열을 문자 '.' 으로 초기화
            for(k = 0; k < input_data[i].weight; k++) {
                result[i][j][k] = '.';
            }
        }
    }
    printf("malloc end\n");
    for(i = 0; i < input_num_total_len; i++) {
        for(j = 0; j < input_data[i].height; j++) {
            for(k = 0; k < input_data[i].weight; k++){
                printf("%c", result[i][j][k]);
            }
            printf(" ");
        }
        printf("\n");
    }

    for(i = 0; i < input_num_total_len; i++) {
        for(j = 0; j < input_data[i].height; j++) {
            free(result[i][j]);
        }
        free(result[i]);
    }
    free(result);

    return 0;
}