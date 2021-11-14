#include <stdio.h>

int visit[1001] = {0};
int arr[4] = {1, 5, 10, 50};
int visit_cnt = 0;
int sum = 0;

void cal(int gen, int N, int cnt) {
    int i = 0;
    
    if(N == cnt - 1) {
        if (visit[sum] == 0) {
            visit[sum] = 1;
            visit_cnt += 1;
            //printf("%d\n", sum);
        }
        return;
    }

    for(i = gen; i < 4; i++ ) {
        sum += arr[i];
        cal(i, N, cnt + 1);
        sum -= arr[i];
    }
}

int main() {
    int N = 0;
    int i = 0;

    scanf("%d", &N);

    cal(0, N, 1);

    printf("%d", visit_cnt);

    return 0;
}