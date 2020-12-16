#include <stdio.h>

using namespace std;
typedef struct pin{
    int x;
    int sum;
    int index;
    int board;
}pin;

int input[10] = {0};
int pin_select[10] = {0};
int finish[4] = {0};
pin my_pin[4];
int max = 0;

int main_board[4][21] = { {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 ,34, 36, 38, 40, 41},
                        {13, 16, 19, 25, 30, 35, 40, 41},
                        {22, 24, 25, 30, 35, 40, 41},
                        {28, 27, 26, 30, 35, 40, 41}};

int check_max() {
    int i = 0, j = 0;
    int cur = 0;
    int dx = 0;

    //for(i = 0; i < 10; i++) printf("%d ", pin_select[i]);
    //printf("\n");

    for(i = 0; i < 4; i++) {
        my_pin[i].x = 0;
        my_pin[i].index = 0;
        my_pin[i].board = 0;
        my_pin[i].sum = 0;
    }

    for(i = 0; i < 10; i++) {
        cur = pin_select[i];
        if(finish[cur] == 0) {
            if(j == 0 && my_pin[cur].x == 10) {
                my_pin[cur].board = 1;
                my_pin[cur].index = 0;
            }
            else if(j == 0 && my_pin[cur].x == 20) {
                my_pin[cur].board = 2;
                my_pin[cur].index = 0;
            }
            else if(j == 0 && my_pin[cur].x == 30) {
                my_pin[cur].board = 3;
                my_pin[cur].index = 0;
            }
            
            for(j = 0; j < input[i]; j++) {
                if (finish[cur] == 0){
                    my_pin[cur].index++;
                    my_pin[cur].x = main_board[my_pin[cur].board][my_pin[cur].index];

                    if(my_pin[cur].x == 41) {
                        finish[cur] = i;
                    }
                }
            }

            int check = 0;
            for(int k = 0; k < 4; k++) {
                if(my_pin[cur].x != 41 && my_pin[cur].board == my_pin[k].board && my_pin[cur].index == my_pin[k].index) check++;
            }
            if(check > 1) {
                return -1;
            }

            if(my_pin[cur].x != 41) my_pin[cur].sum += my_pin[cur].x;
        }
    }

    return my_pin[0].sum + my_pin[1].sum + my_pin[2].sum + my_pin[3].sum;
}

void overlap_com(int cnt) {
    int i = 0;
    int result = 0;

    if(cnt == 10) {
        result = check_max();
        if( max < result) {
            for(i = 0; i < 10; i++) printf("%d ", pin_select[i]);
            printf("\n max = %d, result = %d\n", max, result);
            max = result;
        }
    }

    else {
        for(i = 0; i < 4; i++){
            pin_select[cnt] = i;
            overlap_com(cnt+1);
        }
    }
}

void find_sum(){
    int i = 0;

    //4개의 인자를 가지는 중복 순열
    overlap_com(0);

}

int main() {
    int i = 0;

    for(i = 0; i < 10; i++){
        scanf("%d", &input[i]);
    }

    for(i = 0; i < 4; i++) {
        my_pin[i].x = 0;
        my_pin[i].index = 0;
        my_pin[i].board = 0;
        my_pin[i].sum = 0;
    }
    find_sum();

    printf("%d", max);

    return 0;
}