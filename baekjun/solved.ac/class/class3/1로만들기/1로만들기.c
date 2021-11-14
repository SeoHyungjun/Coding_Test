#include <stdio.h>

int min(int a, int b) {
    if (a <= b) 
        return a;
    else
        return b;
}

int main() {
    int n = 0, i = 0;
    int arr[1000001] = {0};

    scanf("%d", &n);

    for (i=2; i<=n; i++) {
        arr[i] = arr[i-1] + 1;
        if (i%2 == 0)
            arr[i] = min(arr[i], arr[i/2]+1);
        if (i%3 == 0)
            arr[i] = min(arr[i], arr[i/3]+1);            
    }

    printf("%d\n", arr[n]);

    return 0;
}