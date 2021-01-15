#include <iostream>

using namespace std;

int map[1001] = { 0, };

int main() {
    int i = 0, j = 0;
    int N = 0; // 0 <= N <= 1000
    int L = 0, H = 0; // 0 <= L, H <= 1000 // L 가로, H 세로
    
    int max = 0;
    int start = 1001, end = -1;
    int prev_x = 0, prev_y = 0;
    int result = 0;
    int left_end = 0, right_end = 0;

    scanf("%d", &N);

    for(i = 0; i < N; i++) {
        scanf("%d %d", &L, &H);
        map[L] = H;
        
        if (max < H) max = H;

        if (start > L) start = L;
        if (end < L) end = L;
    }

    //printf("max = %d, start = %d, end = %d\n", max, start, end);


    //0부터 max까지
    prev_y = map[start];
    prev_x = start;
    for(i = start; ; i++) {
        if(prev_y < map[i]) {
            //printf("1 i = %d, + %d\n", i, prev_y * (i - prev_x) );
            result += prev_y * (i - prev_x);
            prev_y = map[i];
            prev_x = i;
        }
        if(map[i] == max) break;
    }
    left_end = i;

    //end부터 max까지
    prev_y = map[end];
    prev_x = end;
    for(i = end; ; i--) {
        if(prev_y < map[i]) {
            //printf("2 i = %d, + %d\n", i, prev_y * (prev_x - i) );
            result += prev_y * (prev_x - i);
            prev_y = map[i];
            prev_x = i;
        }
        if(map[i] == max) break;
    }
    right_end = i;

    result += ( (right_end + 1) - left_end ) * max;

    printf("%d", result);


    return 0;
}